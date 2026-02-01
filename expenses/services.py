from django.db.models import Sum
from .models import Expense


def get_monthly_summary(user, year, month):
    expenses = Expense.objects.filter(
        user=user,
        date__year=year,
        date__month=month
    )

    total_spent = expenses.aggregate(total=Sum('amount'))['total'] or 0
    expense_count = expenses.count()

    category_summary = expenses.values('category__name').annotate(
        total_amount=Sum('amount')
    )

    return {
        "year": year,
        "month": month,
        "total_spent": total_spent,
        "expense_count": expense_count,
        "by_category": list(category_summary)
    }
