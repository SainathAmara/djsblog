from django.contrib import admin
from testapp.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields={'slug':('title',)}
    list_filter=('status','author','created','publish')
    search_fields=('title','body')
    raw_id_fields=('author',)
    ordering=['status','publish']
    date_hierarchy='publish'
class CommentAdmin(admin.ModelAdmin):
    list_display=['name','email','post','body','created','updated','active']
    list_filter=('active','created','updated')
    search_fields=('name','email','body')


from testapp.models import hydjobs,chennaijobs,blorejobs,punejobs
# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
class chennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
class blorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']


from testapp.models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['rdate','moviename','hero','heroine','rating']
admin.site.register(Movie,MovieAdmin)

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
admin.site.register(blorejobs,blorejobsAdmin)
admin.site.register(punejobs,punejobsAdmin)

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
