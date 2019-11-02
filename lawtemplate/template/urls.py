from django.urls import path
from .views import Index

urlpatterns = [
    path("egi", Index.as_view())
]
