from django.urls import path

from .views import questions, recommend, create_question, delete_question, update_question, index, get_foods

urlpatterns = [

    path('questions/', questions),  # URL 패턴 변경
    path('create_question/', create_question),
    path('delete_question/<int:question_id>/', delete_question),
    path('update_question/<int:question_id>/', update_question),

    path('recommend/', recommend),

    path('index/', index),

    path('get_foods/', get_foods),

]
