from django.shortcuts import render,HttpResponse

# Create your views here.

#Home
def home(request):

    #context ={
        #'variable1':"This is from variable1 context.",
        #'variable2':"This is from variable2 context.",
        #'variable3':"This is from variable3 context.",
    #}

    #return HttpResponse("This is my home page")
    return render(request, 'index.html')

#About
def about(request):
    return render(request, 'about.html')

#Services
def services(request):
    return render(request, 'services.html')

#Contact
def contact(request):
    return render(request, 'contact.html')

