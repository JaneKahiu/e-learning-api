from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Course, Lesson, Quiz
from .serializers import CourseSerializer, LessonSerializer, QuizSerializer
from rest_framework.views import APIView

class CustomAPIRootView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "courses": "http://127.0.0.1:8000/courses/",
            "lessons": "http://127.0.0.1:8000/lessons/",
            "quizzes": "http://127.0.0.1:8000/quizzes/",
        })

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    #override  create to associate instructor with course
    def perform_create(self, serializer):
        instructor_profile = self.request.user.profile
        serializer.save(instructor=instructor_profile)
    
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # Extra action to grade quiz
    @action(detail=True, methods=['post'])
    def submit_answer(self, request, pk=None):
        quiz = self.get_object()
        answer = request.data.get('answer')
        if quiz.answer.lower() == answer.lower():
            return Response({'message': 'Correct Answer!'}, status=200)
        return Response({'message': 'Incorrect Answer!'}, status=400)               
