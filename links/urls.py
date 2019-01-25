from django.urls import path

from links.views import add_link

urlpatterns = [
    path('', add_link),
]
