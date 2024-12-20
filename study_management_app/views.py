from django.shortcuts import render, redirect

from study_management_app.forms import Add_study_form, Sponsors_add_form
from study_management_app.models import Study


# Create your views here.
def Add_sponsor(request):
    data=Sponsors_add_form()
    if request.method=="POST":
        data = Sponsors_add_form(request.POST)
        if data.is_valid():
            data.save()

            return redirect('studies_list')


    return render(request,'Add_sponsor.html',{'data':data})

def add_study(request):
    data=Add_study_form()
    if request.method=="POST":
        data = Add_study_form(request.POST)
        if data.is_valid():
            data.save()
            return redirect('studies_list')


    return render(request,'Add_study.html',{'data':data})


def studies_list(request):
    study_objects=Study.objects.all()
    return render(request,'Home.html',{'study_objects':study_objects})

def view_study(request,id):
    study_object=Study.objects.get(id=id)
    return render(request, 'view_study.html', {'study_object': study_object})


def edit_study(request,id):
    data=Study.objects.get(id=id)
    data.delete()
    return redirect('studies_list')

def delete_study(request):
    product=Study.objects.all()
    product.delete()
    return redirect('studies_list')


def edit_study(request,id):
    obj=Study.objects.get(id=id)
    form=Add_study_form(instance=obj)
    if request.method=='POST':
        form=Add_study_form(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect(('studies_list'))
    return render(request,'edit_study.html',{'form':form})
