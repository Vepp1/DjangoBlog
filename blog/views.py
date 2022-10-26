from django.shortcuts import render
from django.views import generic
from.models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Postobjects.filter(status=1).order_by('-created_on')
    template_name = 'indext.html'
    paginate_by = 6


