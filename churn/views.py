from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from .models import Data
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponse
import io
from reportlab.pdfgen import canvas 
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.

def Pdf(request):
    # create a Bytestream buffer
    buf = io.BytesIO()
    # create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    # Designate the model
    predict = Data.objects.all()
    # create a blank list
    list = []
    # loop through
    for pred in predict:
        # list.append('Gender: ' +str(pred.gender_display))
        list.append('Tenure: ' +str(pred.tenure))
        list.append('Senior Citizen: ' +str(pred.seniorCitizen_display ))
        list.append('Partner: ' +str(pred.partner_display))
        list.append('Dependents: ' +str(pred.dependents_display))
        list.append('Phone Service: ' +str(pred.phone_service_display))
        list.append('Internet Service: ' +str(pred.internet_service_display))
        list.append('Charges: ' +str(pred.charges))
        list.append('Contract Type: ' +str(pred.contract))
        list.append('Payment Method: ' +str(pred.payment_method))
        list.append('Predictions: ' +str(pred.predictions))
        list.append("=========================================================================")

    for line in list:
        textob.textLine(line)

    # finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    
    # Return the PDF file as response
    return FileResponse(buf, as_attachment=True, filename='print.pdf')
        

def Base(request):
    return render(request, 'base.html')

@login_required(login_url='login')
def Home(request):
    if request.method == 'POST':
        form=DataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('prediction')
    else:    
       form = DataForm()
    context = {
        'form': form
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def Predictions(request):
    pred = Data.objects.all()
    context = {
        'predictions':pred
    }
    return render(request, 'predictions.html', context)

def Register(request):
    if request.method == 'POST':
        reg_form = CreateUserForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('login')
    else:
        reg_form = CreateUserForm()
    context = {
        'reg_form':reg_form
    }
    return render(request, 'register.html', context)

    

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            print("No user")
    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('login')

def Update(request, id):
    if request.method == 'POST':
        if id == 0:
            form=DataForm(request.POST)
        else:
            customer = Data.objects.get(id=id)
            form = DataForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        return redirect('prediction')
    else:
        if id == 0:      
            form = DataForm()
        else:
            customer = Data.objects.get(id=id)
            form = DataForm(instance=customer)
    context = {
        'form': form
    }
    return render(request, 'home.html', context)

def Delete(request, id):
    Data.objects.get(id=id).delete()
    return redirect('prediction')

