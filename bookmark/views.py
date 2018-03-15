from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# 실제로 어떤 기능을 만들어 내는 부분
# 글을 쓸 때, 수정할 때, 지울 때, 볼 때 어떻게 해당 기능이 동작할 것인지

# Create your views here.
from .models import Bookmark

class BookmarkListView(ListView):
    model =  Bookmark

