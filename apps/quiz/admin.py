from django.contrib import admin
from .models import QuesModel, QuizCategoryModel
# Register models
admin.site.register(QuesModel)
admin.site.register(QuizCategoryModel)