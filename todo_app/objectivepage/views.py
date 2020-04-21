from django.shortcuts import render
from objectivepage.models import Objective
from objectivepage.forms import ObjectiveForm

# Create your views here.
def add_object(request):
    form = ObjectiveForm(request.POST or None, initial={'user': request.user})
    if form.is_valid():
        objective = Objective()
        objective.object_name = form.cleaned_data['object_name']
        objective.object_category = form.cleaned_data['object_category']
        objective.user = form.cleaned_data['user']
        objective.save()
        pass
        # ここにリダイレクト処理を追記する（トップへ）まだ、リダイレクト先が無いので未入力

    return render(request, 'objective/object_form.html',{
        'form': form,
    })
