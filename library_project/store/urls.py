from django.conf.urls import url
from django.urls import include, path, re_path

from . import views  # import views to use them in urls


urlpatterns = [
    re_path('^$', views.bookshelf),  # "/store" will call the "index" method in "views.py"
    re_path('^(?P<book_id>[0-9]+)/$', views.details),  # "/store" will call the "index" method in "views.py"
    re_path('^search/$', views.search),  # "/store" will call the "index" method in "views.py"
]
