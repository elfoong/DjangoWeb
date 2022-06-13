from django.shortcuts import render
from web.models import Post


# Create your views here.
def landing(request):
    return render(request, 'single_pages/landing.html',{
        'recent_post' : Post.objects.order_by('-pk')[:3]
    })



def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )
