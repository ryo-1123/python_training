from django.shortcuts import render
from objectivepage.models import Objective
from targetpage.models import Target

# Create your views here.
def display_list(request):
    objectives = Objective.objects.filter(
        user=request.user
    )

    targets = {}
    for num in range(1, 4):
        targets[num] = Target.objects.filter(
            target_status=num
        )

    return render(request, 'listpage/index.html', {
        'objectives': objectives,
        'targets': targets,
    })
