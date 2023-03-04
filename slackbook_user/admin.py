from django.contrib import admin
from .models import Topic
from django_summernote.admin import SummernoteModelAdmin

# admin.site.register(Topic)


@admin.register(Topic)
class TopicAdmin(SummernoteModelAdmin):

    # list_display = ('title', 'slug', 'status', 'created_on')
    # search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    # this crates a filter by status or created_on box
    prepopulated_fields = {'slug': ('title',)}
    # this makes the slug appears automatically
    summernote_fields = ('content',)