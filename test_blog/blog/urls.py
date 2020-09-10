from django.urls import path, re_path
from .views import home, details, login, entry, exit


urlpatterns = [
    path('', home),
    path('home/', home),
    path('login/', login),
    path('entry/', entry),
    path('exit/', exit),
    re_path(r'^details/(?P<iid>[0-9]+)$', details),
]