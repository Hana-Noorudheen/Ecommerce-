
from django.shortcuts import render,redirect
from django.http import request,HttpResponse
from django.contrib.auth.models import User,auth
from django.http import JsonResponse

# Create your views here.


def login(request):
    
    if request.method== 'POST':

        email = request.POST['email']
        password = request.POST['password']

        check_user = auth.authenticate(username=email, password=password)
        
        if check_user:
          u = User.objects.get(username=email)
          Name=u.first_name
          request.session['username'] = Name
          return JsonResponse(

              {'success':True},
               safe=False
             )

        else:    
            
          return JsonResponse(
               {'success':False},
               safe=False
             )      

    else:
        return render(request, 'login.html') 

def signup(request):
    

    if request.method == 'POST':

        Name = request.POST['name']
        Email = request.POST['email']
        Password=request.POST['password']
        ConfirmPassword=request.POST['confirm_password']

        

        if User.objects.filter(email=Email).exists():
            print("Email exists")

            return JsonResponse(

            {'success':False},
              safe=False
            )

        else:

            user = User.objects.create_user(first_name=Name,email=Email,password=Password,username=Email)
            user.save()
            return JsonResponse(
            {'success':True},
            safe=False
            )

    else:    
        return render(request,'signup.html')

def display(request):

  return render(request,'display.html')



  

def logout(request):
  try:
      request.session.flush()
  except:
      return redirect('login')
  

  return redirect('/login')           


