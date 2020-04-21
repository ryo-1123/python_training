from django.shortcuts import render
from targetpage.models import Target
from targetpage.forms import TargetForm
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
