from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article,Category
from .forms import ArticleForm

class Home(View):

    def get(self, request):
        data = Article.objects.all().order_by("-created_at")[:3]
        context = {
            'articles':data,
             
        }
        return render(request, 'main/index.html',context=context)

    def post(self, request):
        return render(request, 'main/index.html')


class ArticleView(View):
    def get(self, request):
        return render(request, 'main/articles.html')

    def post(self, request):
        return render(request, 'main/articles.html')


class ArticleCreate(LoginRequiredMixin,View):
    def get(self, request):
        
        categories = Category.objects.all()

        data = {
            "categories":categories,
            'form':ArticleForm(),
        }

        return render(request, 'main/create.html',context=data)

    def post(self, request):

        data = ArticleForm(data=request.POST,files=request.FILES)

        if data.is_valid():
            title = data.cleaned_data.get('title')
            description = data.cleaned_data.get('description')
            category_id = data.cleaned_data.get('category')
            image = data.cleaned_data.get('image')

            Article.objects.create(
                title = title,
                description = description,
                category = get_object_or_404(Category,pk=category_id),
                image = image,
                author = request.user
            )
            return redirect('home')

        return render(request, 'main/create.html')    