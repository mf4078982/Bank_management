from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from .models import Bank
from .forms import Bankform
from django.shortcuts import get_object_or_404, redirect, render
from decimal import Decimal
# from .forms import DepositForm

# Create your views here.
def add(request):
    stu = Bank.objects.all()
    if request.method == 'POST':
        form = Bankform(request.POST)
        if form.is_valid():
            form.save()
            form = Bankform()  # Clear the form after savin
            # return redirect('show')
    else:
        form = Bankform() 

    return render(request, 'create_account.html', {'forms': form, 'stud': stu})





def show(request):
    accounts = Bank.objects.all()
    return render(request, 'show.html', {'Student': accounts})




def home(request):
    return render(request, 'home.html')


# views.py

# views.py

def deposit(request):
    if request.method == 'POST':
        acc_no = request.POST.get('acc-no')
        amount = request.POST.get('amount')

        try:
            account = Bank.objects.get(acc_no=acc_no)
            account.acc_balance += Decimal(amount)  # Convert amount to Decimal before adding
            account.save()
            return redirect('show')
        except Bank.DoesNotExist:
            # Handle the case where the account number does not exist
            return render(request, 'deposit.html', {'error': 'Account does not exist'})

    return render(request, 'deposit.html')


def withdraw(request):
    if request.method == 'POST':
        acc_no = request.POST.get('acc-no')
        amount = request.POST.get('amount')
        
        # Convert amount to Decimal
        try:
            amount = Decimal(amount)
        
        except ('InvalidOperation', ValueError):
            # Handle invalid amount input
            return render(request, 'withdraw.html', {'error': 'Invalid amount'})
        
        # Retrieve the account object
        account = get_object_or_404(Bank, acc_no=acc_no)
        
        # Ensure acc_balance is Decimal for comparison and arithmetic
        if account.acc_balance >= amount:
            account.acc_balance -= amount
            account.save()
            return redirect('show')
        else:
            # Handle insufficient funds case
            return render(request, 'withdraw.html', {'error': 'Insufficient funds'})
    
    return render(request, 'withdraw.html')


def exit(request):
    
    return render(request, 'exit.html')




def delete(request,id):
    if request.method == 'POST':
        user = Bank.objects.get(pk=id)
        user.delete()
        return HttpResponseRedirect('/')


