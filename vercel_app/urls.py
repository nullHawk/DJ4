import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('ads/', include('ads.urls')),
    path('hello/', include('hello.urls')),
    path('polls/', include('polls.urls')),
    path('puchi/', include('puchi.urls')),
    path('autos/', include('autos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cats/', include('cats.urls')),
    path('secret_santa/', include('secret_santa.urls')),
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns += [
    re_path(r'^site/(?P<path>.*)$', serve, {'document_root': os.path.join(BASE_DIR, 'site'), 'show_indexes': True}, name='site_path'),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path('favicon.ico', serve, {'path': 'favicon.ico', 'document_root': os.path.join(BASE_DIR, 'home/static')}),
]

# Switch to social login if it is configured - Keep for later
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0, path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login)))
    print('Using', social_login, 'as the login template')
except ImportError:
    print('Using registration/login.html as the login template')
