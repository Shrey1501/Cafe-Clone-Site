from django.shortcuts import render
from mysite.forms import ReserveInfoForm

# Create your views here.
def index(request):
    return render(request,'mysite/index.html')

def reserve(request):

    reserved = False
    if request.method == "POST":
        reserve_form = ReserveInfoForm(data=request.POST)

        if reserve_form.is_valid():

            reserve = reserve_form.save(commit=False)
            reserve.save()

            reserved = True

        else:
            print(reserve_form.errors)

    else:
        reserve_form = ReserveInfoForm()

    return render(request,'mysite/reserve.html',{
                    'reserve_form':reserve_form,
                    'reserved':reserved
    })

def serviceone(request):
    return render(request,'mysite/serviceone.html')

def servicetwo(request):
    return render(request,'mysite/servicetwo.html')

def servicethree(request):
    return render(request,'mysite/servicethree.html')        
