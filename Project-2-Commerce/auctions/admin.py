from django.contrib import admin
from .models import Auction, User, Bid, Comment, Watclist, Category

# Register your models here.

admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Watclist)
admin.site.register(Category)
