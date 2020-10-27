from django.shortcuts import render
from django.http import  HttpResponse
from blog.models import   Article

def hello_world(request):
    return HttpResponse("hello world")



def artcle_content(request):
    article = Article.objects.all()[0]
    article_id = article.article_id
    title = article.title
    brief_content = article.brief_content

    return_str = 'title.%s'%(title,brief_content)
    return HttpResponse("return_str")


