from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import (CourseViewSet, LessonCreateAPIView, LessonDeleteAPIView,
                       LessonListAPIView, LessonRetrieveAPIView,
                       LessonUpdateAPIView)

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="courses")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="create_lesson"),
    path("lesson/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="view_lesson"),
    path(
        "lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="update_lesson"
    ),
    path(
        "lesson/delete/<int:pk>/", LessonDeleteAPIView.as_view(), name="delete_lesson"
    ),
] + router.urls
