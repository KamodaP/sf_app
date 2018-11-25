from django.shortcuts import render

# Create your views here.
def galaxy_map(request):
    context = {}
    return render(request, 'starmap/galaxymap.html', context)