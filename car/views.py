from django.shortcuts import render,redirect
from . import models
from django.urls import reverse
def list(request):
    allcars = models.Car.objects.all()
    context = {'allcars': allcars}
   

    return render(request,"car/list.html",context=context)

def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand,year=year)
        return redirect(reverse('car:list'))
    else:
        return render(request,"car/add.html")

def delete(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('car:list'))
        except:
            print("pk not found")
            return redirect(reverse('car:list'))

    return render(request,"car/delete.html")

