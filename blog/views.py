from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView,  CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context={
       # 'posts':posts           #post is the variable sent to the home.html
                                #to access the posts dictionary
          'posts' : Post.objects.all()  #here we are actually removing the dummy data and adding the real time data that we havce just created
    }
    return render(request,'blog/home.html',context)     #here we have pass the context dictionary to access
#class based views is very useful
class PostListView(ListView):
    model = Post        #theses are nothing but the variables and their  values so we can directly apply   anywhere
    template_name = 'blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  #for arranging fPostrom oldest to newest

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
# to validate the form as the previously the auhtor is mandatory
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
# to validate the form as the previously the auhtor is mandatory
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request,'blog/about.html',{'title':'about'})






#    posts=[{
#        'author':'jimmy',                   ITS A LIST OF DICTIONARIES[DUMMY DATA]
#        'title':'Blog post1',
#        'content':'first_post content',  its was a dummy data for instance
#but now we no longer need it as we added real time data
#        'date_posted':'21 feb 2018'
#    },
#        'author':'maje',
        #    {
#        'title':'Blog post_2',
#        'content':'second_post content',
#        'date_posted':'20 feb 2018'
#    } ]
# Create your views here.











#fff
