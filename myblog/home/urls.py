from django.urls import path

from . import views
#neu sau lienhe co / se khong hien images
urlpatterns = [
    path('', views.tatcabaiviet),
    path('lienhe', views.lienhe, name="contacttt"),
    path('baiviet/<int:baiviet_id>', views.baivietcuthe, name="baivietcuthe"),
]