from django.contrib import admin

from .models import Food, Question, Choice


@admin.register(Food)
class FoodModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class uestionModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Choice)
class ChoiceModelAdmin(admin.ModelAdmin):
    pass