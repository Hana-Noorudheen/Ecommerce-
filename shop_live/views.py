
from django.shortcuts import render,redirect
from django.http import request,HttpResponse
from django.contrib.auth.models import User,auth
from django.http import JsonResponse
from admin_app. models import Products,Category,Cart,Order

# Create your views here.


def login(request):
  if request.session.has_key('username'):
    

    return redirect('userdisplay')
    
       

  else:
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

    return render(request, 'login.html')
 

def signup(request):
  if request.session.has_key('username'):
 

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
    name=u.first_name

    if request.method == 'POST':
      id=request.POST['id']
      quantity=request.POST['quantity']
      p=Products.objects.get(id=id)
    
      if Cart.objects.filter(pid=id).exists():
        quantity=int(quantity)

        # quantity+=1

        ct=Cart.objects.filter(pid=id).update(quantity=quantity)
        

      else:  
    
        ct=Cart.objects.create(userid=u,pid=p,quantity=quantity)
        ct.save()

      return redirect('cart')
    else:

      c=Cart.objects.filter(userid=u.id)
      items=c.count()
      return render(request,'users/cart.html',{'cart':c,'items':items,'Name':name})

  else:
    return redirect('login')

def category(request,id):

  c=Category.objects.get(id=id)
  p=Products.objects.filter(category=c)

  return render(request,'users/category.html',{'products':p})



      

def cartcalc(request):

  if request.session.has_key('username'):

    if request.method == 'POST':
      cartid=request.POST['cartid']
      qty=request.POST['qty']
      check=request.POST['check']
      print(check)

      if check=='add':   
        qty=int(qty)
        qty=qty+1
        Cart.objects.filter(id=cartid).update(quantity=qty)
        return JsonResponse(

            {'success':True },
              safe=False
            )

      if check == 'minus':
        qty=int(qty)
        qty=qty-1
      
        Cart.objects.filter(id=cartid).update(quantity=qty)

        return JsonResponse(

            {'success':True },
              safe=False
            )


def order(request,id):
  if request.session.has_key('username'):

    username = request.session['username']
    u= User.objects.get(username=username)
    name=u.first_name

    if request.method == 'POST':

      
      
      Name= request.POST['name']
      address=request.POST['hno']
      city=request.POST['city']
      state=request.POST['state']
      Phone=request.POST['pno']
      pincode=request.POST['pin']
      id=int(id)
      c=Cart.objects.get(id=id)



      Order.objects.create(name=Name,address=address,city=city,state=state,pincode=pincode,Phone=Phone,cartid=c)
      id=int(id)
      
      c=Cart.objects.all()
      return render (request, 'users/payment.html',{'id':id,'cart':c,'Name':name})


    else:
      id=int(id)
      c=Cart.objects.all()
      

      return render(request,'users/order.html',{'id':id,'cart':c,'Name':name})


      
  else:

    return redirect('login')

def logout(request):
  try:
      request.session.flush()
  except:
      return redirect('login')
  

  return redirect('/login')     



