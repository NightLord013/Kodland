from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Entry
from .forms import PostForm

def index(request):
    number = Entry.objects.latest('pubdate')
    entries = Entry.objects.filter().order_by('-pk')[:10]
    return render(request, 'Kodland/home.html', {'entries' : entries, "number": number})

def post_detail(request, pk):
    post = get_object_or_404(Entry, pk=pk)
    return render(request, 'Kodland/post.html', {'post': post})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.pubdate = timezone.now()
            form.save()
            return HttpResponseRedirect('../../')
    else:
        form = PostForm()
    return render(request, 'Kodland/new_post.html', {'form': form})

    

    
