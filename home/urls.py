from django.contrib import admin
from django.urls import path
from home.views import BlogView, PublicBlogView

urlpatterns = [
    path('', PublicBlogView.as_view()),
    path('blog/', BlogView.as_view())
]
