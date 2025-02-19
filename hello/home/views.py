from django.shortcuts import render,HttpResponse

# Create your views here.

#Home
def index(request):

    context ={
        'variable1':"This is from variable1 context.",
        'variable2':"This is from variable2 context.",
        'variable3':"This is from variable3 context.",
    }

    #return HttpResponse("This is my home page")
    return render(request, 'index.html', context)

#About
def about(request):
    return HttpResponse("This is my about page")

#Services
def services(request):
    return HttpResponse("This is my services page")

#Contact
def contact(request):
    return HttpResponse("This is my contact page")

