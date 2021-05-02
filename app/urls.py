# -*- encoding: utf-8 -*-
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, TagDetailView, TagView, AsideView, FeedBackView, RegisterView, ProfileView
from app import views

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path("", include(router.urls)),
    path("tags/", TagView.as_view()),
    path("tags/<slug:tag_slug>/", TagDetailView.as_view()),
    path("aside/", AsideView.as_view()),
    path("feedback/", FeedBackView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),

    # # The home page
    # path('', views.index, name='home'),
    # # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
