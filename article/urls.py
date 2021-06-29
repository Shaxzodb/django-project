from django.urls import path
from .views import AlerListViewPost

urlpatterns = [
    path('',AlerListViewPost.as_view(),name='home'),
]