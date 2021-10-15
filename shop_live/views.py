
from django.shortcuts import render,redirect
from django.http import request,HttpResponse
from django.contrib.auth.models import User,auth
from django.http import JsonResponse
from admin_app. models import Products,Category,Cart

# Create your views here.


def login(request):
    
    if request.method== 'POST':

        email = request.POST['email']
        password = request.POST['password']

        check_user = auth.authenticate(username=email, password=password)
        
        if check_user:
          u = User.objects.get(username=email)
          username = u.username
          request.session['username'] = username
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

def userdisplay(request):
  if request.session.has_key('username'):
    username = request.session['username']
    p=Products.objects.all()
    c=Category.objects.all()
    
    u= User.objects.get(username=username)
    name=u.first_name

    return render(request,'users/index.html',{'products':p,'Name':name,'category':c})
  else:
    return redirect('login')

def product(request,id):
  if request.session.has_key('username'):
    p=Products.objects.all()
    
    id=int(id)


    return render(request,'users/productdetails.html',{'product':p,'pid':id})

def cart(request):
  if request.session.has_key('username'):

    username = request.session['username']
    u= User.objects.get(username=username)

    if request.method == 'POST':
      id=request.POST['id']
      p=Products.objects.get(id=id)
  
      ct=Cart.objects.create(userid=u,pid=p)
      ct.save()

      return redirect('cart')
    else:

      c=Cart.objects.filter(userid=u.id)
      return render(request,'users/cart.html',{'cart':c})

  else:
    pass  



def logout(request):
  try:
      request.session.flush()
  except:
      return redirect('login')
  

  return redirect('/login')     



