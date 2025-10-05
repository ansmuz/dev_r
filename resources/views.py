from django.shortcuts import render
from .models import Tool, Library


def index(request):
    return render(request, 'index.html')




def libraries(request):
    libraries = Library.objects.all()
    return render(request, "libraries.html", {'libraries': libraries})


def tools(request):
    tools = Tool.objects.all()
    return render(request, "tools.html", {'tools': tools,} )