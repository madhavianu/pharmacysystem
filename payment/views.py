from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from medicine.models import Medicine

def create_payment(request):
    if request.method == 'POST':
        # Get form data
        medicine_id = request.POST['medicine_id']
        quantity = int(request.POST['quantity'])
        amount = request.POST['amount']
        payment_method = request.POST['payment_method']

        # Fetch the selected medicine
        medicine = get_object_or_404(Medicine, id=medicine_id)

        # Check if there is enough stock
        if medicine.quantity >= quantity:
            # Deduct the quantity from stock
            medicine.quantity -= quantity
            medicine.save()

            # Save the transaction
            Transaction.objects.create(
                medicine_name=medicine.name,
                quantity=quantity,
                amount=amount,
                payment_method=payment_method
            )
            return redirect('transaction_list')
        else:
            # If not enough stock, show an error
            return render(request, 'create_payment.html', {
                'medicines': Medicine.objects.all(),
                'error': 'Not enough stock available for the selected medicine.',
            })

    # Load medicines for the dropdown
    medicines = Medicine.objects.all()
    return render(request, 'create_payment.html', {'medicines': medicines})

def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-date')
    return render(request, 'transaction_list.html', {'transactions': transactions})
