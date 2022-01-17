from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from bms.forms import NewBookForm,SearchForm
from bms import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import Image
from django.utils.datastructures import MultiValueDictKeyError


def uploader(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.all()
 # return render(request, 'bms/uploader.html', {'form':form})

 return render(request, 'bms/uploader.html', {'img':img, 'form':form})

def userlogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('http://localhost:8000/bms/view-books')
        else:
            data['error']="Username or password is incorrect"
            res=render(request,'bms/login.html',data)
            return res
    else:
        res=render(request,'bms/login.html',data)
        return res






@login_required(login_url='http://localhost:800/bms/login/')
def newBook(request):
    form=NewBookForm()
    res=render(request,'bms/new_book.html',{'form':form})
    return res



@login_required(login_url='http://localhost:8000/bms/login/')
def addBook(request):
    if request.method=='POST' :
        form=NewBookForm(request.POST )
        book=models.Book()
        book.title=form.data['title']
        book.author=form.data['author']
        book.price=form.data['price']
        book.publisher=form.data['publisher']
        book.save()
        books=models.Book.objects.all()
        msg=render(request,'bms/view_books.html',{'books':books})
    else:
        msg="record can not be save in database"
        msg=msg+'<br>  <a href="http://localhost:8000/bms/view-books">View Books</a>'
    return HttpResponse(msg)
    
@login_required(login_url='http://localhost:8000/bms/login/')
def viewBooks(request):
    books=models.Book.objects.all()
    res=render(request,'bms/view_books.html',{'books':books})
    return res
@login_required(login_url='http://localhost/bms/login/')
def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('http://localhost:8000/bms/view-books')


@login_required(login_url='http://localhost:8000/bms/login/')
def edit(request):
    if request.method=="POST":
        form=NewBookForm(request.POST, request.FILES  ,False)
        book=models.Book()
        book.id=request.POST['bookid']
        book.tilte=form.data['title']
        book.author=form.data['author']
        book.price=form.data['price']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponseRedirect('http://localhost:8000/bms/view-books')


@login_required(login_url='http://localhost:8000/bms/login/')
def editBook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'author':book.author,'price':book.price,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'bms/edit_book.html',{'form':form,'book':book})
    return res

@login_required(login_url='http://localhost:8000/bms/login/')
def search(request):
    form=SearchForm(request.POST)
    title=form.data['title']
    books=models.Book.objects.filter(title=title)
    res=render(request,'bms/search_book.html',{'books':books,'form':form})
    return res


@login_required(login_url='http://localhost:8000/bms/login/')
def searchBook(request):
    form=SearchForm()
    res=render(request,'bms/search_book.html',{'form':form})
    return res




def userlogout(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/bms/login/')
