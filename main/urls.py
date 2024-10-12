from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, QuizViewSet, CustomAPIRootView

router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)
router.register('quizzes', QuizViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', CustomAPIRootView.as_view(), name='api-root'),#use the custom api root view
]