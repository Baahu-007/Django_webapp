from django.contrib import admin
from .models import Post

# To show the Post option in our admin page its impportant to add it
#it means we have to nregister it
admin.site.register(Post)
