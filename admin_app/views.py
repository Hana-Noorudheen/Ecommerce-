
from django.shortcuts import render,redirect
from django.http import request,HttpResponse
from django.contrib.auth.models import User,auth
from django.http import JsonResponse
from . models import Products,Category
from django.core.paginator import Paginator

# Create your views here.




def adminlogin(request):
  if request.session.has_key('username'):

    u= User.objects.all()
    return render(request,'display.html',{'result':u}) 



  else:

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
  if request.session.has_key('username'):

    if request.method=='POST':

      
      name=request.POST['q']
      u=User.objects.filter(first_name__icontains=name)
      
    else: 
      u= User.objects.all()

    # Pagination
    paginator=Paginator(u,4)
    page_number=request.GET.get('page')
    u=paginator.get_page(page_number)
    return render(request,'display.html',{'result':u})

  else:
    return redirect('adminlogin')   




def delete(request,username):

  if request.session.has_key('username'):


    u=User.objects.get(username=username)
    u.delete()
    return redirect('display')

  else:
    return redirect('adminlogin') 


def products(request):
  if request.session.has_key('username'):

    if request.method=='POST':


      name=request.POST['q']
      u=Products.objects.filter(name__icontains=name)
    else: 
      u=Products.objects.all()

    
    # Pagination
    paginator=Paginator(u,4)
    page_number=request.GET.get('page')
    u=paginator.get_page(page_number)
    return render(request,'product.html',{'result':u}) 
  else:
    return redirect('adminlogin') 


def productdelete(request,id):
  if request.session.has_key('username'):


    p=Products.objects.get(id=id)
    p.delete() 

    return redirect('products') 

  else:
    return redirect('adminlogin')


def productupdate(request,id):
  if request.session.has_key('username'):
    p=Products.objects.get(id=id)
  
    if request.method == 'POST':
      name=request.POST['name']
      desc=request.POST['desc']
      price=request.POST['price']
      img=request.FILES['img']
      
      p.name=name
      p.desc=desc
      p.price=price
      p.img=img
    
      p.save()
      return redirect('products')

    else:
      name=p.name
      desc=p.desc
      price=p.price
  
      return render(request,'productupdate.html',{'name':name,'desc':desc,'price':price})

  else:
    return redirect('adminlogin')


def addproduct(request):
  if request.session.has_key('username'):



    if request.method == 'POST':
      name=request.POST['name']
      desc=request.POST['desc']
      price=request.POST['price']
      img=request.FILES['img']
      offer=request.POST['offer']
      category=request.POST['category']
      c=Category.objects.get(name=category)
      u = Products.objects.create(name=name,desc=desc,price=price,img=img,offer=offer,category=c)
      u.save()
      
  
    
      return redirect('products')
  
    else:

      c=Category.objects.all()
  
      return render(request,'productadd.html',{'Category':c})

  else:
    return redirect('adminlogin')

    


def update(request,username):

  if request.session.has_key('username'):


    u=User.objects.get(username=username)
    if request.method == 'POST':
      name=request.POST['name']
      email=request.POST['email']
      u.first_name=name
      u.email=email
  
      u.save()
      return redirect('display')
  
    else:
      name=u.first_name
      email=u.email
  
      return render(request,'update.html',{'name':name,'email':email})

  else:
    return redirect('adminlogin')



def logout(request):
  try:
      request.session.flush()
  except:
      return redirect('adminlogin')
  

  return redirect('adminlogin')           



