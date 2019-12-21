from django.shortcuts import render
# Create your views here.
posts = [
    {
        'author' : 'Namra Desai',
        'title' : 'Blog Post 1',
        'content' : 'first post content',
        'date_posted' : 'December 20,2019'
    },
    {
        'author' : 'Poojan Patel',
        'title' : 'Blog Post 2',
        'content' : 'second post content',
        'date_posted' : 'December 21,2019'
    },
]
def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
