from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .api_views import BirthdayModelViewSet, LetterDigitAPIView

router = DefaultRouter()
router.register(r'birthdays', BirthdayModelViewSet, basename='birthday_view')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/get-upper-lowercase-variation/<str:string>/', LetterDigitAPIView.as_view()),
]
