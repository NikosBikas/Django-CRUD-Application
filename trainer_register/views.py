from django.shortcuts import redirect, render
from .forms import TrainerForm
from .models import Trainer

# Create your views here.
def trainer_list(request):
    context = {'trainer_list':Trainer.objects.all()}
    return render(request,"trainer_register/trainer_list.html", context)

def trainer_form(request,id=0):
    if request.method == "GET":
        if id==0:   
            form = TrainerForm()
        else:
            trainer = Trainer.objects.get(pk=id)
            form = TrainerForm(instance=trainer)
        return render(request,"trainer_register/trainer_form.html",{'form':form})
    else:
        if id == 0:
            form = TrainerForm(request.POST)
        else:
            trainer = Trainer.objects.get(pk=id)
            form = TrainerForm(request.POST,instance=trainer)
        if form.is_valid():
            form.save()
        return redirect('/trainer/list')

def trainer_delete(request,id):
    trainer = Trainer.objects.get(pk=id)
    trainer.delete()
    return redirect('/trainer/list')

def rain(request):
    return render(request,"trainer_register/rain.html")