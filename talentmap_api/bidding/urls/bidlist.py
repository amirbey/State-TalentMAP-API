from django.conf.urls import url
from rest_framework import routers

from talentmap_api.common.urls import patch_update
from talentmap_api.bidding.views import bidlist as views

router = routers.SimpleRouter()
router.register(r'', views.BidListView, base_name="bidding.Bid")

urlpatterns = [
    url(r'^position/(?P<pk>[0-9]+)/$', views.BidListPositionActionView.as_view(), name='bidding.Bid-position-actions'),
    url(r'^bid/(?P<pk>[0-9]+)/submit/$', views.BidListBidSubmitView.as_view(), name='bidding.Bid-bid-actions'),
    url(r'^bid/(?P<pk>[0-9]+)/$', views.BidUpdateView.as_view(patch_update), name='bidding.Bid-bid-update'),
]

urlpatterns += router.urls