from django.shortcuts import render, redirect, get_object_or_404
from .models import DoctorGroup
from .forms import DoctorGroupForm
from .forms import CustomUserCreationForm

def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor-groups')  # Redirect to the admin dashboard
    else:
        form = CustomUserCreationForm()
    return render(request, 'dashboard/add_user.html', {'form': form})


def doctor_group_list(request):
    groups = DoctorGroup.objects.all()
    return render(request, 'dashboard/doctor_group_list.html', {'groups': groups})

def add_doctor_group(request):
    if request.method == 'POST':
        form = DoctorGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_group_list')
    else:
        form = DoctorGroupForm()
    return render(request, 'dashboard/doctor_group_form.html', {'form': form})

def edit_doctor_group(request, pk):
    group = get_object_or_404(DoctorGroup, pk=pk)
    if request.method == 'POST':
        form = DoctorGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('doctor_group_list')
    else:
        form = DoctorGroupForm(instance=group)
    return render(request, 'dashboard/doctor_group_form.html', {'form': form})
