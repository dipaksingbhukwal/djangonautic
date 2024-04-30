from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', { 'articles': articles })

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', { 'article': article })

# Decorator 'login_required' requires login before rendering article_create page.
# Once user login, redirected to create page.
@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # Add the author to article first, then save article and redirect
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("articles:list")
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {"form":form})