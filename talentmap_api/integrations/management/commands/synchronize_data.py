from django.core.management.base import BaseCommand

import logging
import os

from django.core.management import call_command

from talentmap_api.integrations.models import SynchronizationJob


class Command(BaseCommand):
    help = 'Synchronizes all eligible SynchronizationJobs'
    logger = logging.getLogger('console')

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument('--list', dest='list', action='store_true', help='Lists all synchronization jobs')
        parser.add_argument('--model', nargs='?', dest="model", help='Used to specify a model to load only the specifically requested model')

    def handle(self, *args, **options):
        if options['list']:
            for job in list(SynchronizationJob.objects.all()):
                print(job)
            return

        jobs = SynchronizationJob.get_scheduled()

        if options['model']:
            jobs = jobs.filter(talentmap_model=options['talentmap_model'])

        for job in list(jobs.all()):
            job.synchronize()

        self.logger.info("Now updating relationships...")
        call_command('update_relationships')
        self.logger.info("Updating string representations...")
        call_command("update_string_representations")
