from django.shortcuts import render,redirect
from .models import Customer,Transaction_history
from system.forms import customerbalanceform
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def customer(request):
    customer=Customer.objects.all()

    return render(request,'news.html',{'customer':customer})

def transaction(request,pk):
    customer=Customer.objects.all()
    return render(request,'transaction.html',{'customer':customer,'id':pk})

def transaction_history(request,pk2):
    sender=Customer.objects.filter(id=pk2)[0]
    reciever=Transaction_history.objects.filter(sender_id=pk2)
    
    
    return render(request,'transaction_history.html',{'reciever_detail':reciever,'sender_balance':sender.balance})

def make_transaction(request,pk1):
    if request.method =='POST':
        sender= Customer.objects.filter(id=pk1)[0]
        
        reciever=request.POST['reciever']
        
    
        reciever1=Customer.objects.filter(name=reciever)[0]
        amount=request.POST['amount']
        if int(sender.balance)> int(amount):
            
            transaction_history=Transaction_history(reciever=reciever,amount=amount,sender=sender)
            transaction_history.save()
            
            sender_balance=int(sender.balance)-int(amount)
            sender.balance=sender_balance
            sender.save()
            
            reciever_balance=int(reciever1.balance)+int(amount)
            reciever1.balance=reciever_balance
            reciever1.save()
            customer=Customer.objects.all()

            return render(request,'news.html',{'customer':customer})
        else:
            messages.info(request,"Sender have Insuffecient Balance. !!")
            customer=Customer.objects.all()
            return render(request,'news.html',{'customer':customer})
def delete_history(request,pk3):
    
    history=Transaction_history.objects.filter(id=pk3).delete()
    customer=Customer.objects.all()
    return redirect('customer')

def delete_customer(request,pk3):
    history=Customer.objects.filter(id=pk3).delete()
    return redirect('customer')