from django.contrib.auth.views import LogoutView
from django.urls import path
from . views import *


app_name = "PR"
urlpatterns = [
    path("", MainPageView.as_view(), name="main_page"),
    path("storage/", PageStorageView.as_view(), name="stoargepage"),
    path("add_impression/", AddImpressionView.as_view(), name="add_page"),
    path("logout/", LogoutView.as_view(), name="logout"),

]
