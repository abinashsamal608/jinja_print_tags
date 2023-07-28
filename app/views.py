from django.shortcuts import render

# Create your views here.

def data_render(request):
    d = {'Name':'ABINASH', 'Course':'Python FullStack', 'B_Code':'PYD-M2','Age':23}

    return render(request, 'data_render.html', context =d)

def if_cond(request):
    d = {'a':100,'b':120}
    return render(request, 'if_cond.html', context = d)

