from django.urls import path
from . import views

urlpatterns = [
    path('', views.tagged_items_view, name='tagged_items'),
]
