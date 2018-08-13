from django.conf.urls import url
from . import views
#
urlpatterns = [
    url(r'^accounts/profile/$', views.home),
    url(r'^accounts/profile/BirdHitForm/$', views.bird_hit_form_func),
    url(r'^accounts/profile/IncidentForm/$', views.incident_form_func),
    url(r'^accounts/profile/BirdHitReport/$', views.bird_form_submitted),
    url(r'^accounts/profile/birdHitAnalysis/$', views.bird_hit_analysis),
    url(r'^accounts/profile/view/(?P<form_id>\d+)/', views.form_view),
    url(r'^accounts/profile/view/(?P<username>\d+)/', views.form_view),
    url(r'^accounts/profile/user/', views.user_view),
    url(r'^accounts/profile/birdHitAnalysis/map/', views.map_view),
    # url(r'accounts/profile/MaxStats/', views.map_view)
]
