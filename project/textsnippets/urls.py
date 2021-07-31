
from django.conf.urls import url
from textsnippets import views

urlpatterns = [

    url('tags/$', views.TagsDetails.as_view()),
    url('textsnippets/$', views.TextsnippetDetail.as_view()),
    url('textsnippetdatadetails/(?P<pk>[0-9]+)/$', views.TextsnippetDataDetails.as_view()),
    url('tagsearch/$', views.Tagdata.as_view()),

]

