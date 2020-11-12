from app import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:id>/', views.item_view, name='item')
]
