from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from newapp.forms import TrainerForm, DietPlanForm
from newapp.models import Trainer, DietPlan

@login_required(login_url='login_view')
def trainer_home(request):
    return render(request, "trainer/trainer_base.html")


@login_required(login_url='login_view')
def trainer_profile(request):
    data = Trainer.objects.get(trainer=request.user)
    return render(request, 'trainer/trainer_profile.html', {'data': data})





@login_required(login_url='login_view')
def trainer_profile_update(request, id):
    data = Trainer.objects.get(id=id)
    form = TrainerForm(instance=data)

    if request.method == "POST":
        form = TrainerForm(request.POST, instance=data)

        if form.is_valid():
            form.save()
            return redirect("trainer_profile")

    return render(request,"trainer/trainer_profile_update.html",{"form": form})


@login_required(login_url='login_view')
def add_diet_plan(request):
    form = DietPlanForm()

    if request.method == "POST":
        form = DietPlanForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.trainer = Trainer.objects.get(trainer=request.user)
            data.save()
            return redirect('trainer_diet_plans')

    return render(request, 'trainer/diet_plan.html', {'form': form})



@login_required(login_url='login_view')
def trainer_diet_plans(request):
    trainer = Trainer.objects.get(trainer=request.user)
    data = DietPlan.objects.filter(trainer=trainer)

    return render(request, 'trainer/trainer_diet_plan.html', {'data': data})