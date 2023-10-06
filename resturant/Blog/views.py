from django.shortcuts import render, get_object_or_404
from .models import Blog, Tag, Category, Comment
from django.views import View
from .forms import CommentForm
from django.core.paginator import Paginator


class Blog_list(View):
    def get(self, request):
        blogs = Blog.objects.all()
        paginator = Paginator(blogs, 3)
        page_number = request.GET.get("page")
        blog_list = paginator.get_page(page_number)

        return render(request, 'blog/blog.html', {'blog_list': blog_list})


class Blog_detail(View):
    form_class = CommentForm

    def setup(self, request, *args, **kwargs):
        self.blog_instance = Blog.objects.get(pk=kwargs['id'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, id):
        blog = self.blog_instance
        tags = Tag.objects.all().filter(blogs=blog)
        categories = Category.objects.all()
        comments = Comment.objects.all().filter(blog=blog)
        recents = Blog.objects.all().order_by("-created")[:5]
        return render(request, 'blog/blog-details.html',
                      {'blog': blog, "tags": tags, "recents": recents, "categories": categories, "comments": comments})

    def post(self, request, id):
        blog = self.blog_instance
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            new_comment = Comment(blog=blog, name=name, email=email, text=text)
            new_comment.save()
        return render(request, 'blog/blog-details.html', {'form': form})


class Blog_tag(View):
    def get(self, request, tag):
        blogs = Blog.objects.all().filter(tag__slug=tag)
        paginator = Paginator(blogs, 3)
        page_number = request.GET.get("page")
        blog_list = paginator.get_page(page_number)
        return render(request, 'blog/blog.html', {'blog_list': blog_list})


class Blog_category(View):
    def get(self, request, category):
        blogs = Blog.objects.all().filter(category__slug=category)
        paginator = Paginator(blogs, 3)
        page_number = request.GET.get("page")
        blog_list = paginator.get_page(page_number)
        return render(request, 'blog/blog.html', {'blog_list': blog_list})


class search(View):
    def get(self, request):
        if request.method == "GET":
            q = request.GET.get("search")
        blog_list = Blog.objects.filter(title__icontains=q)
        return render(request, 'blog/blog.html', {'blog_list': blog_list})
