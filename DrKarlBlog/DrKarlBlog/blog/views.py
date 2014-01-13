from django.shortcuts import render_to_response

from DrKarlBlog.models import post

def home(request):
	entries = post.objects.all()[:10]
	return render_to_response("index.html", {'post': entries})