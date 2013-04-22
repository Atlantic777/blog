from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Post

def blog_roll(request):
	post_list = Post.objects.order_by('-datetime')
	return render_to_response('blog_roll.html', {'post_list':post_list})

def blog_single_post(request, post_id):
	post = Post.objects.get(pk=post_id)
	return render_to_response('blog_single_post.html', {'post':post})
