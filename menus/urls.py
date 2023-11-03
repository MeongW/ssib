from django.urls import path

from .views import questions, recommend, create_question, delete_question, update_question

urlpatterns = [

    path('questions/', questions),  # URL 패턴 변경
    path('create_question/', create_question),
    path('delete_question/', delete_question),
    path('update_question/', update_question),

    path('recommend/', recommend),


]
