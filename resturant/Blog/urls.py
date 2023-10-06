from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.Blog_list.as_view(), name='blog_list'),
    path('<int:id>', views.Blog_detail.as_view(), name='blog_detail'),
    path('tags/<slug:tag>', views.Blog_tag.as_view(), name='blog_tag'),
    path('categorys/<slug:category>', views.Blog_category.as_view(), name='blog_category'),
    path('search/', views.search.as_view(), name='search'),
]
