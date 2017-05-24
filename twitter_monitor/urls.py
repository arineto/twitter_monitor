from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^djangojs/', include('djangojs.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    url(r'^logout/$',
        auth_views.logout,
        {'next_page': 'login'},
        name='logout'),

    url(r'^login/$',
        TemplateView.as_view(template_name='core/login.html'),
        name='login'),

    url(r'^$',
        login_required(TemplateView.as_view(template_name='core/index.html')),
        name='home'),

    url(r'^api/v1/monitor/', include('monitor.api.urls', namespace='monitor')),
]
