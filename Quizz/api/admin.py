from django.contrib import admin
from .models import *


class AnswerChoice(admin.TabularInline):
    model = Answer
    extra = 0


class AdminQuestion(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question', 'q_image', 'q_level', 'q_category']}),
    ]
    inlines = [AnswerChoice]

admin.site.register(Question, AdminQuestion)