from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Food


class HomeView(View):
    # form_class = PostSearchForm

    def get(self, request):
        foods = Food.objects.all()
        # if request.GET.get('search'):
        #     foods = foods.filter(body__contains=request.GET['search'])
        return render(request, 'food/index.html', {'foods': foods})

    def post(self, request):
        return render(request, 'food/index.html')


class FoodsDetail(View):
    def get(self, request, food_id):
        food = Food.objects.get(id=food_id)
        return render(request, 'food/detail.html', {"food": food})


class Menu(View):
    # form_class = PostSearchForm

    def get(self, request):
        foods = Food.objects.all()
        # if request.GET.get('search'):
        #     foods = foods.filter(body__contains=request.GET['search'])
        return render(request, 'food/menu.html', {'foods': foods})


class About(View):
    def get(self, request):
        foods = Food.objects.all()
        return render(request, 'food/about.html', {'foods': foods})


class Gallery(View):
    def get(self, request):
        return render(request, 'food/gallery.html')
