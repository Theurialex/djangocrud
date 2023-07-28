from django.shortcuts import render, redirect
from crudProject1.models import Student
from crudProject1.forms import StudentForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            form = StudentForm()
            return render(request, 'index.html', {'form': form})


def show(request):
    Student = student.objects.all()
    return render(request, 'show.html', {'student': Student})


def edit(request, id):
    Student = Student.objects.get(id=id)
    return render(request, 'edit.html', {'student': Student})


def delete(request, id):
    Student = Student.objects.get(id=id)
    return redirect('/show')


def update(request, id):
    Student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=Student)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'student': Student})
