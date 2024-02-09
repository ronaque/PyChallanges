from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
from cryptography_app.models import Cryptography
import hashlib

def index(request, iterator):
    return HttpResponse("Hello, world. You're at the cryptography index iterator %d." % iterator)

def create_cryptography(request, userDocument, creditCardToken, value):
    userDocument = hashlib.sha512(userDocument.encode('utf-8')).hexdigest()
    creditCardToken = hashlib.sha512(creditCardToken.encode('utf-8')).hexdigest()
    cryptography = Cryptography(userDocument=userDocument, creditCardToken=creditCardToken, value=value)
    cryptography.save()
    serialized_crypto = serialize("json", Cryptography.objects.filter(pk=cryptography.pk))
    serialized_crypto = json.loads(serialized_crypto)
    return JsonResponse(serialized_crypto, safe=False, status=200, json_dumps_params={'indent': 2})

def list_all_cryptography(request):
    query_crypto = Cryptography.objects.all()
    serialized_crypto = serialize("json", query_crypto)
    serialized_crypto = json.loads(serialized_crypto)
    return JsonResponse(serialized_crypto, safe=False, status=200, json_dumps_params={'indent': 2})