from django.view.generic import View
from django.shortcuts import render
from .models import Post

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.object.order_by("-id")
        return render(request, 'app/index.html', {
            'post_data' : post_data,
        })