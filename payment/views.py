import json

import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from cart.cart import Cart
from orders.views import payment_confirmation


@login_required
def basket_view(request):
    cart = Cart(request)
    total = str(cart.get_total_price())
    total = total.replace(".", "")
    total = int(total)

    stripe.api_key = settings.STRIP_SECRET_KEY
    intent = stripe.PaymentIntent.create(amount=total, currency="gbp", metadata={"userid": request.user.id})
    return render(request, "payment/home.html", {"client_secret": intent.client_secret})


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None
    print(1234567)

    try:
        event = stripe.Event.construct_from(json.loads(payload), stripe.api_key)
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == "payment_intent.succeeded":
        payment_confirmation(event.data.object.client_secret)
        print("yes worked")

    else:
        print("Unhandled event type {}".format(event.type))

    return HttpResponse(status=200)


def order_placed(request):
    cart = Cart(request)
    cart.clear()
    return render(request, "payment/orderplaced.html")
