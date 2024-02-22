from django.contrib import admin
from .models import Post, Category
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Comment

@admin.register(Comment)
class CommentAdminPage(DjangoMpttAdmin):
    """
    Админ панель модели комментариев
    """
    pass

@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {'slug': ('title', )}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
