from django.shortcuts import render
from objectivepage.models import Objective
from targetpage.models import Target

# Create your views here.
def display_list(request):
    objectives = Objective.objects.filter(
        user=request.user
    ).order_by('id').reverse()

    targets = {
        1: [],
        2: [],
        3: [],
    }
    for objective in objectives:
        for num in range(1, 4):
            target = Target.objects.filter(
                target_status=num,
                objective=objective,
            ).order_by('id').reverse()
            targets[num] += list(target)

    """
    11~22行目のbetterな書き方

    targets = defaultdict(list)
    q_target = Target.objects.filter(objective__user=request.user).order_by('target_status')
    for target in q_target:
        targets[target.target_status].append(target)
    """

    print(targets)
    return render(request, 'listpage/index.html', {
        'objectives': objectives,
        'targets': targets,
    })
