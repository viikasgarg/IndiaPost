from django.http import JsonResponse
from postalcode.models import PostalCode
import math

SERVICE_TAX = 1.15
MATRTIX = {
    "DLH": {'fd': 30, 'vr': 8},
    "NCR": {'fd': 40, 'vr': 10},
    "STC": {'fd': 70, 'vr': 18},
    "MAC": {'fd': 80, 'vr': 20}
}


def get_charge(pin, weight):
    try:
        p = PostalCode.objects.get(pincode=pin)
    except PostalCode.DoesNotExist:
        return None
    if p.deliverystatus != "Delivery":
        return None
    weight_slab = math.ceil(weight / 500)
    pricing = MATRTIX[(p.pricing_code)]
    charge = pricing['fd'] + (weight_slab - 1) * pricing['vr']
    return charge


def home(request, *args, **kwargs):
    weight = request.GET.get('weight')
    pin = request.GET.get('pin')

    try:
        weight = float(weight)
        pin = int(pin)
        if pin < 100000 or weight > 5000:
            raise
    except:
        return JsonResponse({'error':
            'Please Pass weight as float number (gm) and less than 5000 and Pincode as 6 digit integer'
                             })

    charge = get_charge(pin, weight)
    if charge:
        return JsonResponse({'charge': charge})
    else:
        return JsonResponse(
            {'error': "{} pincode is not servicable".format(pin)})
