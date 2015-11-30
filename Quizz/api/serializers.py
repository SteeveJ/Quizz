from rest_framework import serializers, viewsets
from .models import *


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question


# ViewSets define the view behavior.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer


# ViewSets define the view behavior.
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer