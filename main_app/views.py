from django.shortcuts import render, get_object_or_404
from .models import Entry

def index(request):
    entries = Entry.objects.all()
    number = entries.count() + 1
    return render(request, 'Kodland/home.html', {'entries' : entries, "number": number})

def post_detail(request, pk):
    post = get_object_or_404(Entry, pk=pk)
    return render(request, 'Kodland/post.html', {'post': post})
    
