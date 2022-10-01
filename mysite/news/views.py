from django.shortcuts import render, get_object_or_404

from .forms import NewsForm
from .models import News, Category


def index(request):
    news = News.objects.all()
    # categories = Category.objects.all()
    context = {
        "news": news,
        "title": "Список новостей",
        # "categories": categories
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    # categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        "news": news,
        # "categories": categories,
        "category": category
    }
    return render(request, 'news/category.html', context)


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        "news_item": news_item
    }
    return render(request, 'news/view_news.html', context=context)


def add_news(request):
    if request.method == 'POST':
        pass
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', context={'form': form})
