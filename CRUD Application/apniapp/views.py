from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer
from django.contrib import messages
from django.db.models import Q
def home(request):
    query = request.GET.get('search', '')
    C = Customer.objects.all()
    if query:
        C = Customer.objects.filter(
            Q(First_name__icontains=query) |
            Q(Last_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(Email__icontains=query) |
            Q(birth_date__icontains=query) |
            Q(membership__icontains=query) |
            Q(points__icontains=query)
        )
        
        
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the same page or another page after saving
    else:
        form = CustomerForm()
    
    return render(request, 'index.html', {'form': form,'Customers':C})



def delete(request, id):
    r = Customer.objects.get(pk=id)
    try:
        r.delete()
    except:
        messages.add_message(request, messages.ERROR,
                                 "Did not work!")
    return redirect('home')

def edit(request, id):
    
    r = Customer.objects.get(pk=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=r)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Your Data has been changed Successfully!")
            return redirect('home')

    else:
        form = CustomerForm(instance=r)
    return render(request, 'index.html', {'form': form})