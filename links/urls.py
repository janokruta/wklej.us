from django.urls import path

from links.views import add_link, link_detail

urlpatterns = [
    path('', add_link),
    path('<slug:slug>', link_detail, name='link_detail'),
]
