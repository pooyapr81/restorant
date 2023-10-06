from django.urls import path
from . import views

app_name = 'reservation'
urlpatterns = [
    path('', views.ReservView.as_view(), name='reservation'),
    # path('food/<int:food_id>/', views.FoodsDetail.as_view(), name='fooddetail')
]
