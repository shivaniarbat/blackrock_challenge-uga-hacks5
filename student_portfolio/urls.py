from django.urls import path
from student_portfolio import views

urlpatterns = [
    path('', views.student_portfolio, name = 'student_portfolio'),
]