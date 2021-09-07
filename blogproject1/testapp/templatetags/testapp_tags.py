from django.db.models import Count
from django import template
from testapp.models import Post
register=template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()
@register.inclusion_tag('testapp/latestposts.html')
def show_latest_posts():
    latest_posts=Post.objects.order_by('-publish')[:4]
    return {'latest_posts':latest_posts}
@register.inclusion_tag('testapp/latestposts.html')
def get_most_commented_posts():
    latest_comments=Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:3]
    return {'latest_comments':latest_comments}
