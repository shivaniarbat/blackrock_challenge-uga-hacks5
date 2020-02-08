from django.shortcuts import render
from student_portfolio.app_logic.app_logic import dummy_post_request

# Create your views here.
def student_portfolio(request):
    dummy_post_request()
    return render(request, 'studentportfolio.html', {})



