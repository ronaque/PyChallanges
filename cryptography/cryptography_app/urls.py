from django.urls import path

from cryptography_app import views

urlpatterns = [
    path('index/<int:iterator>', views.index, name='index'),
    path('list_all_cryptography', views.list_all_cryptography, name='list_all_cryptography'),
    path('create_cryptography/<str:userDocument>/<str:creditCardToken>/<int:value>', views.create_cryptography, name='create_cryptography'),
]