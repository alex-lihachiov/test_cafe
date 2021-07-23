from django.contrib import admin

# Register your models here.


from .models import Cafe, Category, Photos, RatingStar, Rating, Reviews

admin.site.register(Category)
admin.site.register(Photos)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
admin.site.register(Cafe)