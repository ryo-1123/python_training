from django.shortcuts import render
from objectivepage.models import Objective

# Create your views here.
def display_list(request):
    objectives = Objective.objects.filter(
        user=request.user
    )

    return render(request, 'listpage/index.html', {
        'objectives': objectives,
    })
