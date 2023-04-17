from django.urls import path
from . import views

urlpatterns = [
    path('', views.Base, name='base'),
    path('home/', views.Home, name='home'),
    path('predictions/', views.Predictions, name='prediction'),
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('update/<str:id>', views.Update, name = 'edit'),
    path('delete/<str:id>', views.Delete, name='delete'),
    path('pdf/', views.Pdf, name='pdf')
]