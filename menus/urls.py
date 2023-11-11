from django.urls import path

from .views import questions, recommend, create_question, delete_question, update_question, index, foods

urlpatterns = [

    path('questions/', questions),
    path('create-question/', create_question),
    path('delete-question/<int:question_id>/', delete_question),
    path('update-question/<int:question_id>/', update_question),

    path('recommend/', recommend),

    path('index/', index),

    path('foods/', foods),

]
