from rest_framework import serializers

from talentmap_api.common.serializers import PrefetchedSerializer
from talentmap_api.organization.models import Organization, Post, TourOfDuty, Location


class OrganizationSerializer(PrefetchedSerializer):
    bureau_organization = serializers.SerializerMethodField()
    parent_organization = serializers.SerializerMethodField()
    highlighted_positions = serializers.StringRelatedField(many=True)
    location = serializers.StringRelatedField()

    # This method returns the string representation of the bureau, or the code
    # if it doesn't currently exist in the database
    def get_bureau_organization(self, obj):
        if obj.bureau_organization:
            return str(obj.bureau_organization)
        else:
            return obj._parent_bureau_code

    # This method returns the string representation of the parent org, or the code
    # if it doesn't currently exist in the database
    def get_parent_organization(self, obj):
        if obj.parent_organization:
            return str(obj.parent_organization)
        else:
            return obj._parent_organization_code

    class Meta:
        model = Organization
        fields = "__all__"


class LocationSerializer(PrefetchedSerializer):
    representation = serializers.SerializerMethodField()

    def get_representation(self, obj):
        return str(obj)

    class Meta:
        model = Location
        fields = "__all__"


class PostSerializer(PrefetchedSerializer):
    code = serializers.CharField(source="_location_code", read_only=True)
    location = serializers.StringRelatedField()
    tour_of_duty = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = "__all__"


class TourOfDutySerializer(PrefetchedSerializer):

    class Meta:
        model = TourOfDuty
        fields = "__all__"
