
from django.shortcuts import render,redirect
from django.http import request,HttpResponse
from django.contrib.auth.models import User,auth
from django.http import JsonResponse

# Create your views here.




def adminlogin(request):

    if request.method== 'POST':

        email = request.POST['email']
        password = request.POST['password']

        u=User.objects.get(username=email)
        if u.is_superuser==True:

            check_user = auth.authenticate(username=email, password=password)
        
            if check_user:
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
            return JsonResponse(
                   {'success':False},
                   safe=False
                 ) 

    
    else:   
        
        return render(request, 'admin.html') 


def display(request):

  return render(request,'display.html')    
  

def logout(request):
  try:
      request.session.flush()
  except:
      return redirect('adminlogin')
  

  return redirect('adminlogin')           



