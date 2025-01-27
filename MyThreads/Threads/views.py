from django.shortcuts import render
from .models import mythread
from .forms import threadform ,userRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login,logout

# Create your views here.

#what are views? Django views are Python functions that take http requests and return http response, like HTML documents.
#what is the use of request and response? In short, the request object is central to handling HTTP requests in Django and
#  is used to access and process all the data associated with the request.

#whereas render In summary, render is a core function in Django that simplifies rendering HTML templates and dynamically passing context data to them.
 
def thread_list(request):
    threads=mythread.objects.all().order_by('-created_at') #here mythread is the model from which we are accessing all the object of the mythread
    #class with the help of objects.all, and order by is use to order the data and the attribute is given in string according which we need the order 
    return render(request,'thread_list.html',{'threads':threads}) #here the context data is given only in dictionary

@login_required
def thread_create(request):     
    if request.method=='POST':#we use request method as post because we are accessing the data from the form
        # If the request method is POST, it indicates that the client is sending data to the server (often through a form submission or an API request).
        form=threadform(request.POST,request.FILES) #this is the meathod to access the form and requsest.FILES help us in accessing the files as well
        if form.is_valid(): #checks is the form is valid and handles the security measures
           thread= form.save(commit=False) #here with commit=False stop the form to send the data to database and just save the data
           #for time being 
           thread.user=request.user #append the user details
           thread.save()
           return redirect('thread_list') #here the method where we need to redirect the page should be given in strings

    else:
        form = threadform()
        return render(request,'thread_form.html',{'form':form})
@login_required  
def edit_thread(request, thread_id): #this meathod is used to edit a thread , it takes an additional argument thread_id to select which
    #thread you want to edit.
    thread=get_object_or_404(mythread,pk=thread_id,user=request.user) #primary key is thread_id, and user= request.user
    if request.method=='POST':
       form=threadform(request.POST,request.FILES,instance=thread) 
       if form.is_valid():
           thread=form.save(commit=False)
           thread.user= request.user    
           thread.save()
           return redirect('thread_list')
    else:
        form=threadform(instance=thread) #here instance= thread is given to check that there should be a data in a form to edit it.
    return render(request,'thread_form.html',{'form':form})

    
@login_required    
def thread_delete(request,thread_id):
    thread= get_object_or_404(mythread,pk=thread_id,user=request.user)
    if request.method=="POST":
        thread.delete()
        return redirect('thread_list')
    return render(request,'thread_confirm_delete.html',{'thread':thread})


def user_registration(request):
    if request.method=='POST':
        form=userRegistrationForm(request.POST)
        if form.is_valid():
           user=form.save(commit=False)
           user.set_password(form.cleaned_data['password1'])   
           user.save()
           login(request,user)
           return(redirect('thread_list'))
    else:
        form= userRegistrationForm()


    return render(request,'registration/register.html',{'form':form})

 