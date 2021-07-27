from . import views
from django.urls import path

app_name = 'core'
urlpatterns = [
    path('form/', views.CoreView.as_view(), name="core-form"),
    path('look', views.CoreApiView.as_view())

]
