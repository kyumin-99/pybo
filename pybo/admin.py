from django.contrib import admin
from .models import Question


# 모델 검색 기능
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)