from django.conf.urls import url, include
from api import views

urlpatterns = [
    url('profile', views.Profilegetpost, name='profile'),
    url('FeedGetPostData', views.FeedGetPostData, name='FeedGetPostData'),
    # url('jobpostapi', views.jobpostapi, name='jobpostapi'),
    url('deleteUser/(?P<pk>[0-9]+)',views.deleteUser,name='deleteuser'),
    url('deleteUser/(?P<pk>[0-9]+)',views.deleteUser,name='deleteuser'),
    url('getsingleuserdata/(?P<pk>[0-9]+)', views.getsingleuserdata, name='getsingleuserdata'),
    url('deletefeedData/(?P<pk>[0-9]+)', views.deletefeedData, name='deletefeedData'),
    url('getsinglefeedinfo/(?P<pk>[0-9]+)',views.getsinglefeedinfo,name='getsinglefeedinfo'),
    url('VolunteerJoinEventApi/(?P<userid>[0-9]+)/(?P<pk>[0-9]+)',views.VolunteerJoinEventApi,name='VolunteerJoinEventApi'),
    url('eventattendiesdata/(?P<pk>[0-9]+)',views.eventattendiesdata,name='eventattendiesdata'),
    # url('deleteWorkerData/(?P<pk>[0-9]+)',views.deleteUser,name='deleteWorkerData'),
    # url('getallactivejobdataforuser/(?P<pk>[0-9]+)',views.getallactivejobdataforuser,name='getallactivejobdataforuser'),
    # url('workerhomepagedata/(?P<pk>[0-9]+)',views.workerhomepagedata,name='workerhomepagedata'),
    url('logininfo/',views.logininfo,name='logininfo'),


]