# -*- encoding: utf-8 -*-
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet
from app import views

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path("", include(router.urls)),
    # # The home page
    # path('', views.index, name='home'),
    # # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
