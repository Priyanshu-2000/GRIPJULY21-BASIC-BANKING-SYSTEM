from django.shortcuts import render, redirect
from django.contrib import messages
from bank.models import Customer, Transaction
from bank.forms import CustomerForm, TransactionForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class CustomerListView(ListView):
    model = Customer

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    redirect_field_name = 'bank/customer_list.html'

class TransactionListView(ListView):
    model = Transaction
    context_object_name = 'transaction_list'
    template_name = 'transfer_list.html'

def Transfer(request):
    customer = Customer.objects.all()
    if request.method=="POST":
        s_acc = request.POST.get('s_acc')
        amt = request.POST.get('amt')
        amt = int(amt)
        r_acc = request.POST.get('r_acc')
        s_bal = Customer.objects.get(account_number = s_acc).balance
        r_bal = Customer.objects.get(account_number = r_acc).balance
        if(amt>s_bal):
            messages.warning(request,f"Insufficient Balance!!!")
            return render(request,'transaction.html',{'customer':customer})
            # return render(request,'transaction.html',{'customer':customer})
        else:
            q1 = Transaction(sender_name=Customer.objects.get(account_number = s_acc), receiver_name = Customer.objects.get(account_number = r_acc), amount = amt)
            q1.save()
            q2 = Customer.objects.filter(account_number=s_acc).update(balance=s_bal-amt)
            # q2.save()
            q3 = Customer.objects.filter(account_number=r_acc).update(balance=r_bal+amt)
            # q3.save()
            messages.success(request,f"Transaction complete")

        return redirect('transfer_list')



        print(s_acc)
        print("HELLO")
        print(amt)
        print(r_acc)


    return render(request,'transaction.html',{'customer':customer})
