import email
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from datetime import datetime
# Create your views here.

# CA signup form
def SignupView(self):
    if self.POST:
        Name = self.POST['name']
        print(Name)
        Email = self.POST['email']
        print(Email)
        Number = self.POST['number']
        print(Number)
        Password = self.POST['password']
        print(Password)
        ConfirmPassword = self.POST['confirmPassword']
        print(ConfirmPassword)

        try:
            data=CasignUp.objects.filter(email=Email)
            if data:
                msg = 'Email already taken'
                return render(self , 'signup.html',{'msg':msg})

            elif ConfirmPassword == Password:
                v = CasignUp()
                v.name = Name
                v.email = Email
                v.number = Number
                v.password = Password
                v.confirmPassword = ConfirmPassword
                v.save()
                return redirect('CALOGIN')

            else:
                msg = 'Enter Same Password'
                return render(self , 'signup.html',{'msg':msg}) 
                
        finally:
            messages.success(self, 'Signup Successfully Done...')

    return render(self,'signup.html')
# ca login
def login(self):
    if self.POST:
        em = self.POST.get('email')
        pass1 = self.POST.get('password')
        try:
            print("Inside first try block")
            check = CasignUp.objects.get(email = em)
            print("Email is ",em,check.email)
            if check.password == pass1:
                # print(check.Password)
                self.session['email'] = check.email
                # return redirect('CADASHBOARD')
                return redirect('home')
                # nameMsg = CasignUp.objects.get(email = em)
                # msg = 'User Successfully logged in'
                # print(msg)
                # return render(self, 'dashboard.html', {'key':nameMsg})
            else:
                return HttpResponse('Invalid Password')
        except:
            print("Inside first except block")
            return HttpResponse('Invalid Email ID')

    return render(self,'login.html')

def userLogOut(request):
    del request.session['email']
    print('User logged out')
    return redirect('CALOGIN')

def contact(request):
    key = ''
    if request.method == 'POST':
        db = ContactForm(fname = request.POST.get('first-name'),
                            lname = request.POST.get('last-name'), 
                            email = request.POST.get('email'), 
                            number = request.POST.get('phone'), 
                            details = request.POST.get('message'))

        db.save()
        key = "Your Message has been sent successfully"
    return render(request, 'contact.html', {'msg': key})

def home(request):
    if 'email' in request.session:
        return render(request, 'home.html')
    return redirect('CALOGIN')

def blog(request):
    if 'email' in request.session:
        return render(request, 'blog.html')
    return redirect('CALOGIN')


def faq(request):
    if 'email' in request.session:
        return render(request, 'FAQ.html')
    return redirect('CALOGIN')


# -----------------------For CHAT-----------------------------------
def index(request):
    return render(request, 'index.html')

def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]
    return render(request, 'room.html', {'room_name': room_name, 'username': username, 'messages': messages})

