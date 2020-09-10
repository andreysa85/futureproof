from django.urls import path, re_path
from .views import admin_panel, edit_post, add_post, delete_post

urlpatterns = [
    path('', admin_panel),
    path('admin_panel', admin_panel),
    path('add_post', add_post),
    re_path(r'^edit_post/(?P<iid>[0-9]+)$', edit_post),
    re_path(r'^delete_post/(?P<iid>[0-9]+)$', delete_post),

]