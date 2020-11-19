from app import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', views.ListUserView.as_view(), name='users'),
    path('detail/<int:pk>/', views.DetailUserView.as_view(), name='detail'),
    path('edit/<int:id>/', views.EditUserView.as_view(), name='edit'),
    path('remove/<int:id>/', views.RemoveUserView.as_view(), name='remove'),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('about/', views.AboutView.as_view(), name='about'),
]
