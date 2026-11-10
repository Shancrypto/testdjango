# from django.shortcuts import render
#
# # Create your views here.
# def home(request):
#     return render(request,"home.html")
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return render(request,"product.html")
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    age= 85
    weight = 33.99
    subjects = ["Maths", "Science", "Engineering"]
    isdisable = False
    name = "Sharon Obiri"

    data ={
        "age": age,
        "weight": weight,
        "subject": subjects,
        "isdisable": isdisable,
        "name":name
    }
    return render(request, 'product.html')
