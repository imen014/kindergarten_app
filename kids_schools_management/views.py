from django.shortcuts import render, get_object_or_404, redirect
from kids_schools_management.forms import Kids_schoolForm, Updater_school_instance
from kids_schools_management.models import Kids_school
from django.contrib.auth.decorators import login_required


@login_required
def create_school(request):
    form = Kids_schoolForm()
    message = ''
    if request.method == "POST":
        form = Kids_schoolForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'school created succefully !'
        else:
            message = 'verify data of school !'
    return render(request, 'kids_schools_management/school_created.html', context={'message':message, 'form':form})

def get_schools(request):
    schools = Kids_school.objects.all()
    return render(request, 'kids_schools_management/get_schools.html', context={'schools':schools})

@login_required
def update_school(request, id):
    school_instance = get_object_or_404(Kids_school, id=id)
    form=Updater_school_instance(instance=school_instance)
    message = ''
    if request.method == "POST":
        form=Updater_school_instance(request.POST, instance=school_instance)
        if form.is_valid():
            form.save()
            message = 'school modified succefully !'
        else:
            message = 'verify data!'
    return render(request, 'kids_schools_management/school_modified.html', context={'message':message,'form':form})

@login_required
def delete_school(request, id):
    school_instance = get_object_or_404(Kids_school, id=id)
    school_instance.delete()
    return redirect('get-schools')






