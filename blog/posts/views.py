from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here
from .models import Post
from .forms import PostForm

def post_list(request):
	queryset = Post.objects.all();
	context ={
		"object_list":queryset,
		"Title":"Posts List"
	}
	return render(request,"home.html",context)

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect("/posts/")
	context ={
		"title":"Add New Post",
		"form" :form
	}
	return render(request,"create.html",context)	