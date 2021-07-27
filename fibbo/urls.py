from django.urls import path
from .views import FibboApiView

app_name = "fibbo"

urlpatterns = [
    path('fib/<int:num>/', FibboApiView.as_view(), name="fibbo-num")
]
