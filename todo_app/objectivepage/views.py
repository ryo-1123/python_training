from django.shortcuts import render, get_object_or_404, redirect
from objectivepage.models import Objective
from objectivepage.forms import ObjectiveForm

# Create your views here.
def add_object(request):
    form = ObjectiveForm(request.POST or None, initial={'user': request.user})
    if form.is_valid():
        form.save()
        return redirect('list:display_list')

    return render(request, 'objective/object_form.html',{
        'form': form,
    })


def edit_object(request, object_id):
    objective = get_object_or_404(Objective, id=object_id)
    if request.method == 'POST':
        form = ObjectiveForm(request.POST, instance=objective)
        if form.is_valid():
            form.save()
            return redirect('list:display_list')
    else:
        form = ObjectiveForm(instance=objective)
    return render(request, 'objective/edit_form.html',{
        'form': form,
        'objective': objective,
    })
