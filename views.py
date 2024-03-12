from django.shortcuts import render,redirect
from newapp.models import categorydb,bookdb
from frontend.models import contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def indexpage(request):
    return render(request,"index.html")
def addcategorypage(request):
    return render(request,"AddCategory.html")

def savecategory(request):
    if request.method == "POST":
        # na = request.POST.get('name')
        # ana = request.POST.get('aname')
        ca = request.POST.get('category')
        ds = request.POST.get('description')
        # ln = request.POST.get('language')
        im = request.FILES['image']

        # pr = request.POST.get('price')
        obj = categorydb(Category=ca,Description=ds,Category_Image=im)
        obj.save()
        messages.success(request, "Category Addedd Successfully...!")
        return redirect(addcategorypage)

def displaycategory(request):
    data = categorydb.objects.all()
    return render(request, "DisplayCategory.html", {'data': data})

def editcategory(request,dataid):
    data=categorydb.objects.get(id=dataid)
    return render(request,"EditCategory.html",{'data':data})

def deletecategory(request,dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Category Deleted...!")
    return redirect(displaycategory)

def updatecategory(request,dataid):
    if request.method=="POST":
        # na = request.POST.get('name')
        # ana = request.POST.get('aname')
        ca = request.POST.get('category')
        ds = request.POST.get('description')
        # la = request.POST.get('language')
        try:
            img=request.FILES['image']
            fs= FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=dataid).Category_Image

        pr = request.POST.get('price')
        categorydb.objects.filter(id=dataid).update(Category=ca,Description=ds,Category_Image=file)
        return redirect(displaycategory)

def addbookpage(request):
    data=categorydb.objects.all()
    return render(request,"AddBook.html",{'data':data})

def savebook(request):
    if request.method == "POST":
        ca = request.POST.get('category')
        bna = request.POST.get('bname')
        ana = request.POST.get('aname')
        la = request.POST.get('language')
        de = request.POST.get('description')
        pr = request.POST.get('price')
        im = request.FILES['image']
        obj = bookdb(Category=ca,Book_Name=bna,Author_Name=ana,Language=la,Description=de,Price=pr,Book_Image=im)
        obj.save()
        messages.success(request, "Book Addedd Successfully...!")
        return redirect(addbookpage)

def displaybook(request):
    data = bookdb.objects.all()
    return render(request, "DisplayBook.html", {'data': data})

def editbook(request,reader_id):
    data=categorydb.objects.all()
    reader=bookdb.objects.get(id=reader_id)
    return render(request,"EditBook.html",{'data':data,'reader':reader})

def deletebook(request,dataid):
    data=bookdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Book Deleted...!")
    return redirect(displaybook)

def updatebook(request,reader_id):
    if request.method=="POST":

        ca = request.POST.get('category')
        bna = request.POST.get('bname')
        ana = request.POST.get('aname')
        ds = request.POST.get('description')
        la = request.POST.get('language')
        pr = request.POST.get('price')
        try:
            img=request.FILES['image']
            fs= FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=bookdb.objects.get(id=reader_id).Book_Image
            bookdb.objects.filter(id=reader_id).update(Category=ca,Book_Name=bna,Author_Name=ana,Description=ds,Language=la,Price=pr,Book_Image=file)
        return redirect(displaybook)

def adminloginpage(request):
    return render(request,"Adminloginpage.html")

def adminlogin(request):
    if request.method=="POST":
        un=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(indexpage)
            else:
                return redirect(adminloginpage)
        else:
            return redirect(adminloginpage)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminloginpage)


def displaycontactdetails(request):
    data=contactdb.objects.all()
    return render(request,"DisplayContactDetails.html",{'data':data})

def deletecontact(request,dataid):
    data=contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontactdetails)

def editcontact(request,dataid):
    data=contactdb.objects.get(id=dataid)
    return render(request,"EditContact.html",{'data':data})

def updatecontact(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        nu = request.POST.get('number')
        em = request.POST.get('email')
        ad = request.POST.get('address')
        me = request.POST.get('message')
        contactdb.objects.filter(id=dataid).update(Name=na,Number=nu,Email=em,Address=ad,Message=me)
        return redirect(displaycontactdetails)
