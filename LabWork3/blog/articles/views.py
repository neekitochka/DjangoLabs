from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from articles.models import Article


def archive(request):
    return render(request, 'templates/archive.html', {"posts": Article.objects.all()})
