# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
from django.views.generic import TemplateView

admin.autodiscover()


# Robots and humans (http://humanstxt.org/)
# -----------------------------------------------------------------------------
robots = lambda _: HttpResponse('User-agent: *\nDisallow:\n', mimetype='text/plain')
humans = lambda _: HttpResponse(u"""/* TEAM */
    Main developer: YOUR NAME            # FIXME: set main developer name -- humans.txt
    Contact: contact [at] yourdomain.com # FIXME: set main developer email -- humans.txt
    From: YOUR LOCATION                  # FIXME: set main developer location -- humans.txt

/* SITE */
    Language: English                    # FIXME: set site language(s) -- humans.txt
    Backend: Python, Django, SQLite      # FIXME: set site backend stack -- in humans.txt
""", mimetype='text/plain; charset=UTF-8')

urlpatterns = patterns('',
    url(r'^robots.txt$', robots, name='robots-txt'),
    url(r'^humans.txt$', humans, name='humans-txt'))

# Applications and pages
# -----------------------------------------------------------------------------
urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'))

# Static / Media
# -----------------------------------------------------------------------------
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
