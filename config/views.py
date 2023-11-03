from django.http import HttpResponseNotFound
from django.http import HttpResponse

def view_404(request, exception):
    return HttpResponseNotFound("Sorry, the page you are looking for does not exist.")

def questions(request):
    return HttpResponse("This is the questions view.")
