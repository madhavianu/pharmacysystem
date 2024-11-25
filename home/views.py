from django.shortcuts import redirect, render
#from .models import Medicine
#from .forms import MedicineForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home_page(request):
    return render(request,'home_page.html')