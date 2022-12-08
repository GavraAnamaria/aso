from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Mesaj
from django.template import loader
from .forms import FormMsg
from django.contrib.auth import logout

def logoutView(request):
    logout(request)
    return redirect('login')


def index(request):
    if request.method == 'POST':
        form = FormMsg(request.POST, request.FILES)
 
        if form.is_valid():
            mesaj = form.save(commit=False)
            mesaj.user = request.user
            mesaj.save()
            return redirect('index')
    else:
        form = FormMsg()
    latest_question_list = Mesaj.objects.all()
    context = {'latest_question_list': latest_question_list, 'form': form}
    return render(request, 'aso/index.html', context)
    
