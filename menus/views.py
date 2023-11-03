from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Question, Food, Choice
from .serializers import QuestionSerializer

import random

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
    recommended_food_name=[k for k, v in scores.items() if max(scores.values()) == v]
    recommended_food_name = random.choice(recommended_food_name)
    return Response({'recommended_food': recommended_food_name})