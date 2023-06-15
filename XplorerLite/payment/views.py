from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PaymentForm
from .models import Payment

@login_required
def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save(commit=False)  # Create a Payment object but don't save it yet
            payment.user = request.user  # Assign the logged-in user as the owner of the payment
            payment.save()  # Save the Payment object to the database
            return redirect('payment:success')
    else:
        form = PaymentForm()
    
    context = {
        'form': form,
    }
    return render(request, 'payment/pay.html', context)

@login_required
def success_view(request):
    payment_id = request.session.get('payment_id')
    if payment_id:
        payment = Payment.objects.filter(id=payment_id).first()
        if payment:
            payment.image.delete()  # Delete the image associated with the Payment object
            payment.delete()  # Delete the Payment object itself

    # Clear the session data
    request.session.pop('payment_id', None)

    return render(request, 'payment/success.html')