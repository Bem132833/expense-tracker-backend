from django.urls import path
from .views import ExpenseListCreateAPIView, MonthlySummaryAPIView

urlpatterns = [
    path('expenses/', ExpenseListCreateAPIView.as_view()),
    path('expenses/monthly-summary/', MonthlySummaryAPIView.as_view()),
]
