from rest_framework import serializers
from .models import Profile, Course, Lesson, Quiz
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    instructor = ProfileSerializer(read_only=True)
    
    class Meta:
        model = Course
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    
    class Meta:
        model = Lesson
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    
    class Meta:
        model = Quiz
        fields = '__all__'
    