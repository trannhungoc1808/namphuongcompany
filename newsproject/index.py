from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def homevietnamese(request):
    return render(request, 'basevietnamese.html')

def homeenglish(request):
    return render(request, 'base.html')

def specialpomelo(request):
    return render(request, 'Products-details.html')

def pomelotype1(request):
    return render(request, 'Products-details2.html')

def pomelotype2(request):
    return render(request, 'Products-details3.html')

def pdetailsvie(request):
    return render(request, 'Products-detail-Vie.html')

def pdetails2vie(request):
    return render(request, 'Products-details2-Vie.html')

def pdetails3vie(request):
    return render(request, 'Products-details3-Vie.html')

def transport(request):
    return render(request, 'Transport.html')

def transportvie(request):
    return render(request, 'Transport-Vie.html')

#def contact(request):
    #return render(request, 'contact.php')
