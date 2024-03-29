from django import template
from blog.models import Post, Tag


register = template.Library()


@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts": posts}


@register.inclusion_tag('blog/tags_cloud_tpl.html')
def get_tags_cloud():
    tags = Tag.objects.all().order_by('title')
    return {"tags": tags}
