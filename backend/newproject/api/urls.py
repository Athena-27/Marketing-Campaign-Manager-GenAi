from django.urls import path
from . import views

urlpatterns = [
    path('campaign/<str:campaign_id>/', views.get_campaign_details_view, name='campaign-details'),
    path('campaign/<str:campaign_id>/generated_post', views.get_instagram_post_view, name='generated-post'),
    path('campaigns/', views.list_campaigns_view, name='list-campaigns'),
    path('campaign/generate/', views.generate_instagram_post_view, name='generate-campaign'),
]
