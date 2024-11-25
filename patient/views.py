from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm

# View to show patient records
def patient_list(request):
    patients = Patient.objects.all()
    for patient in patients:
        print(f'Patient ID: {patient.id}')  # Debugging line
    return render(request, 'patient_list.html', {'patients': patients})

# View to add a patient
def patient_add(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')  # Redirect to the patient list page
    else:
        form = PatientForm()
    return render(request, 'patient_add.html', {'form': form})




# View to edit a patient's details
def patient_edit(request, id):
    try:
        patient = Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        return redirect('patient_list')  # Redirect back if patient not found

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')  # Redirect to the list page after editing
    else:
        form = PatientForm(instance=patient)  # Pre-fill the form with existing patient data

    return render(request, 'patient_edit.html', {'form': form, 'patient': patient})






# View to delete a patient's record
def patient_delete(request, id):
    patient = Patient.objects.get(id=id)  # Get the patient record by ID
    patient.delete()  # Delete the patient record from the database
    return redirect('patient_list')  # Redirect back to the patient list
