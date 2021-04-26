# -*- encoding: utf-8 -*-
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, TagDetailView, TagView
from app import views

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path("", include(router.urls)),
    path("tags/", TagView.as_view()),
    path("tags/<slug:tag_slug>/", TagDetailView.as_view()),

    # # The home page
    # path('', views.index, name='home'),
    # # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
