from django.http import HttpResponse

def home(request):
    return HttpResponse("Adair says Hello!")