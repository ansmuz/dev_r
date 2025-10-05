from django.shortcuts import render
from resources.models import Tool, Library

def index(request):
    tools = Tool.objects.all()
    libraries = Library.objects.all()
    return render(request, 'index.html', {'tools': tools, 'libraries': libraries})

