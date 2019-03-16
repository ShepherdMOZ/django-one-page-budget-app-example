from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from .forms import NewTransactionForm
from .models import Transaction

# Create your views here.
class MainPageView(View):
    template_name = 'BudgetCalc/index.html'
    form_class = NewTransactionForm
    transactions = Transaction.objects.all()
    

    def get(self,request,*args, **kwargs):
        return render(request, self.template_name, {'form':self.form_class, 'table':self.transactions})
    
    def post(self,request,*args, **kwargs):
        submit_form = self.form_class(data=request.POST)
        if submit_form.is_valid():
            submit_form.save()
            return render(request, self.template_name, {'form':self.form_class, 'table':self.transactions})
        
        return render(request, self.template_name, {'form':submit_form, 'table':self.transactions})