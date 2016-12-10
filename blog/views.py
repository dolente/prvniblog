from django.shortcuts import render
from blog.models import Post #tohle jsme taky přihodili napodruhý...


def post_list(request):
    posts = Post.objects.all() #tohle jsme sem přihodili později :) současně s níže ""posts": posts"
    return render(request, 'blog/post_list.html', {"posts": posts}) #tohle jsme sem přihodili, ale moc nevim co si k tomu napsat

# Create your views here.
