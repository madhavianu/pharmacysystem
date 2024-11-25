from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine
from .forms import MedicineForm
from django.http import HttpResponse

def medi_list(request):
    medicines = Medicine.objects.all()  # Fetch all medicines
    return render(request, 'medi_list.html', {'medicines': medicines})

def medi_add(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medi_list')
    else:
        form = MedicineForm()
    return render(request, 'medi_add.html', {'form': form})

def medi_edit(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medi_list')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'medi_edit.html', {'form': form})

def medi_delete(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        medicine.delete()
        return redirect('medi_list')
    return HttpResponse("Invalid request method", status=405)
