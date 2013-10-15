from django.conf.urls import patterns, include, url

from questions.views import QuestionsListView

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',   
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'', include('social_auth.urls')),
    url(r'^questions/', include('questions.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^comments/', include('django.contrib.comments.urls')),

    url(r'^accounts/profile/$', QuestionsListView.as_view(), name='list'),

    url(r'^password/reset/$', 
        'django.contrib.auth.views.password_reset', 
        { 'post_reset_redirect' : '/password/reset/done/'},
        name="password_reset"),

    url(r'^password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),

    url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/password/done/'}),

    url(r'^password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),

    
)
