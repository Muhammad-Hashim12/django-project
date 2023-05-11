from django.shortcuts import render,HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('Hello I am here')


def current_page(request):
    return render(request,'ind.html')

def add(request):
    num1=request.POST['num1']
    num2=request.POST['num2']
    res=int(num1)+int(num2)
    context = {
        'result':res
        }
    return render(request,'result.html',context)    