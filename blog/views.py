from django.http import JsonResponse
from .models import BlogPost, Comment
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts = BlogPost.objects.all().values()
        return JsonResponse(list(posts), safe=False)

@csrf_exempt
def post_detail(request, pk):
    try:
        post = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author.username
        })

@csrf_exempt
def comment_list(request, pk):
    if request.method == 'GET':
        comments = Comment.objects.filter(post_id=pk).values()
        return JsonResponse(list(comments), safe=False)
