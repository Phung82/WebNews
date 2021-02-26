from django.urls import path
from . import views

#urlpatterns laf 1 LIST luu cac duong dan
urlpatterns = [
    path('', views.index),
    path('contact/', views.v_contact, name='contacttt'),
    path('about/', views.v_about,name="abouttt"),
    path('post/', views.v_post,name="posttt"),

]
