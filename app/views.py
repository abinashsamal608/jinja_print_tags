from django.shortcuts import render

# Create your views here.

def data_render(request):
    d = {'Name':'ABINASH', 'Course':'Python FullStack', 'B_Code':'PYD-M2'}

    return render(request, 'data_render.html', context =d)
