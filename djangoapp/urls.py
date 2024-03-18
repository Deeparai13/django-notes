from django.urls import path
from djangoapp import views


urlpatterns = [ 
    path('', views.base, name="base"),
    path('abc/', views.post, name="post"),
    path("detail/<int:pk>",views.detail, name="detail"),

    path('bc/', views.gallery, name="gallery"),
    path('add/', views.contact, name="contact"),  
] 