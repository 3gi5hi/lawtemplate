from django.urls import path
from .views import Index, AddTemplates

urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("addtemplates/", AddTemplates.as_view(), name="addtemplates")
]
