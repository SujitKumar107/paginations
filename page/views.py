from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

from .serializers import PostSerialiser
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerialiser

# Create your views here.
def home(request):
    data=Post.objects.all()
    paginator=Paginator(data,2)
    print("Paginator:",paginator)

    page_no=request.GET.get('page')
    print('Page Num:',page_no)

    page_obj=paginator.get_page(page_no)
    print('Page Obj :',page_obj)

    return render(request,'home.html',{'dt':page_obj})
