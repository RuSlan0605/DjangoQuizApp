from django.contrib import admin
from .models import Quiz

class UserAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

@admin.register(Quiz)
class QuestionAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'question']
    list_display_links = ['id', 'question']

