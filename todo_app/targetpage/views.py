from django.shortcuts import render, get_object_or_404, redirect
from targetpage.models import Target
from targetpage.forms import TargetForm, TargetEditForm
from pprint import pprint

# Create your views here.
def create_target(request):
    form = TargetForm(request.POST or None)
    print(form.errors)
    if form.is_valid():
        form.save()
        # ここにリダイレクト処理を追記する（トップへ）まだ、リダイレクト先が無いので未入力

    return render(request, 'target/create_form.html',{
        'form': form,
    })


def edit_target(request, target_id):
    target = get_object_or_404(Target, id=target_id)
    if request.method == 'POST':
        form = TargetEditForm(request.POST, instance=target)
        if form.is_valid():
            form.save()
            return redirect('list:display_list')
    else:
        form = TargetEditForm(instance=target)
    return render(request, 'target/edit_form.html',{
        'form': form,
        'target': target,
    })
