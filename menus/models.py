from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200, default='Default Question Text')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    foods_positive = models.ManyToManyField(Food, related_name='choices_positive')
    foods_negative = models.ManyToManyField(Food, related_name='choices_negative')

    def __str__(self):
        return self.text
