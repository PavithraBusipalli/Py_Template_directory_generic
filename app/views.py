from django.shortcuts import render
# Create your views here.

def view1(request):
    return render(request,'html1.htm')

def view2(request):
    return render(request,'html2.htm')

def view3(request):
    return render(request,'html3.htm')

def view4(request):
    return render(request,'html4.htm')