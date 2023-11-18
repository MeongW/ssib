from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Question, Food, Choice
from .serializers import QuestionSerializer, FoodSerializer

from django.shortcuts import render

import random

# 음식 데이터 가져오기 (GET 요청 처리)
@api_view(['GET'])
def foods(request):
    id = request.GET.get('id')
    foods = Food.objects.get(pk=id)
    serializer = FoodSerializer(foods)
    return Response(serializer.data)

def index(request):
    return render(request, 'recommends.html')

@api_view(['GET'])
def questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


# 새로운 질문 생성 (POST 요청 처리)
@api_view(['POST'])
def create_question(request):
    serializer = QuestionSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# 특정 질문 수정 (PUT 요청 처리)
@api_view(['PUT'])
def update_question(request, question_id):
    question = Question.objects.get(id=question_id)
    
    serializer = QuestionSerializer(question, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# 특정 질문 삭제 (DELETE 요청 처리)
@api_view(['DELETE'])
def delete_question(request, question_id):
    question = Question.objects.get(id=question_id)
    question.delete()

    return Response({'message': 'Question was deleted successfully!'}, status=204)


@api_view(['POST'])
def recommend(request):
    responses_ids=request.POST.getlist('responses')
    scores={}
  
    for response_id in responses_ids:
        choice=Choice.objects.get(id=response_id)
      
        for food in choice.foods_positive.all():
            if food.name not in scores:
                scores[food.name]=1 # 해당되면 +1점 부여 
            else: 
                scores[food.name]+=1
      
        for food in Food.objects.exclude(id__in=[f.id for f in choice.foods_positive.all()]):
            if food.name not in scores:
                scores[food.name]=-10 # 해당되지 않으면 -10점 부여
            else:
                scores[food.name]-=10

    first = ''
    second = ''

    try:
        recommended_food_name=[k for k, v in scores.items() if max(scores.values()) == v]
        first, second = random.sample(recommended_food_name, 2)
    except:
        recommended_food_name=[k for k, v in scores.items() if max(scores.values()) == v]

    first = recommended_food_name.pop()
    del scores[first]

    recommended_food_name = [k for k, v in scores.items() if max(scores.values()) == v]
    second = random.choice(recommended_food_name)


    first_object = Food.objects.get(name=first)
    second_object = Food.objects.get(name=second)

    print(scores)
    return Response({'recommended_food': { 'first': first_object.id, 'second': second_object.id }})
