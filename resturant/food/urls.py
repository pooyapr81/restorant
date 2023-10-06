from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.HomeView.as_view(), name='food'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('about/', views.About.as_view(), name='about'),
    path('gallery/', views.Gallery.as_view(), name='gallery'),
    path('food/<int:food_id>/', views.FoodsDetail.as_view(), name='fooddetail')
]
