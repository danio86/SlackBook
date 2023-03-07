from django.contrib import admin
from .models import Channel, Topic, Post
from django_summernote.admin import SummernoteModelAdmin


# admin.site.register(Channel)


@admin.register(Channel)
class ChannelAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Topic)
class TopicAdmin(SummernoteModelAdmin):

    list_display = ('title',)
    # list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    # list_filter = ('status', 'created_on')
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('user', 'channel', 'body', 'created_on')
    # list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    # list_filter = ('created_on')
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
