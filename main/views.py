from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import authenticate,login,logout

from .models import Article,Category
from .forms import ArticleForm, ArticleModelForm

from django.core.paginator import Paginator
from django.db.models import Q

class Home(View):

    def get(self, request):
        data = Article.objects.all().order_by("-created_at")
        search = request.GET.get("search")
        if search:
            data = data.filter(Q(title__icontains=search)| Q(description__icontains = search))
        
        context = {
            'articles':data[:3],
             
        }
        return render(request, 'main/index.html',context=context)

    def post(self, request):
        return render(request, 'main/index.html')


class ArticleView(View):
    def get(self, request):
        articles = Article.objects.all()

        category = request.GET.get('category')

        if category:
            articles = articles.filter(category__name=category)

        paginator = Paginator(articles,3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'main/articles.html',context={"articles":page_obj})

    def post(self, request):
        return render(request, 'main/articles.html')


class ArticleCreate(LoginRequiredMixin,View):
    def get(self, request):
        
        categories = Category.objects.filter(is_active=True)
        forms = ArticleForm()

        context = {
            "categories":categories,
            'form':forms,
        }

        return render(request, 'main/create.html',context=context)

    def post(self, request):
        categories = Category.objects.filter(is_active=True)

        data = ArticleModelForm(data=request.POST,files=request.FILES)

        if data.is_valid():

            data = data.save(commit=False)
            data.author = request.user

            data.save()
            
            return redirect('articles')
        
        context = {
            "categories": categories,
            "form":data
        }
        return render(request, 'main/create.html',context=context)  
    
class LoginView(View):
    def get(self,request):
            
        return render(request,'main/auth/login.html')

    def post(self,request):

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)
        if user:
            login(request,user)

            return redirect("create")
            
        return render(request,'main/auth/login.html')
        
