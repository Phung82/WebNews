from django.urls import path
from . import views

#urlpatterns laf 1 LIST luu cac duong dan
urlpatterns = [
    path('',views.index),
]
