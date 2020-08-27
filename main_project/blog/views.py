from django.shortcuts import render

posts = [
    {
        'author': 'David',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'August 26, 2020'
    },
    {
        'author': 'Davide',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'August 27, 2020'
    }
]


# Create your views here.
def home(request):
    contex = {
        'posts': posts
    }
    return render(request, 'blog/home.html', contex)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})