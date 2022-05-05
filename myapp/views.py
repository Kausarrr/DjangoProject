from django.shortcuts import render, redirect
from .forms import EmpForm
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .import models

def add_emp(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request, "polls/from.html", {"form":form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            return redirect('/admin')
        else:
            clear_errors = form.errors.get("all")
            return render(request, "polls/from.html", {"form": form, "clear_errors": clear_errors})

from django.shortcuts import render

def send_message(request):
    email=EmailMessage(
              "Hallo",
              "My content",
              "200103312@stu.sdu.edu.kz",
              ['200103312@stu.sdu.edu.kz','200103199@stu.sdu.edu.kz'],
              headers={'Message-ID':'foo'},
        )
    email.attach_file('/Users/сулпак/Pictures/IMG_20200322_145445_mh1584872148746.jpg')
    email.send(fail_silently=False)
    return render(request,'polls//success.html')
