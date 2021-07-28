from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JIF4PI3vCZO9P2g0DR8gRgjXKwM13IxtgB2bbkYtSAPFyJuahVqjPIs1u7Yc128N5swACplxWX4ESykRbOZoNOc00f2ODbE1d',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
