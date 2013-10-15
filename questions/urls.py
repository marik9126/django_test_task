#coding: utf-8
from django.conf.urls import patterns, url

from questions.views import QuestionsListView, QuestionDetailView, CreateQuestion, CompleteCreateQuestion

urlpatterns = patterns('',
url(r'^$', QuestionsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/question/ 
                                               # будет выводиться список постов
url(r'^(?P<pk>\d+)/$', QuestionDetailView.as_view()), # а по URL http://имя_сайта/question/число/ 
                                              # будет выводиться пост с определенным номером
url(r'^create/$', CreateQuestion.as_view()),

url(r'^create/complete/$', CompleteCreateQuestion.as_view()),

)