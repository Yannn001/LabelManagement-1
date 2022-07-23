from django.shortcuts import render
from .models import Package

def package_detailed_view(request):
    obj = Package.objects.get(package_ID = "7d31a64e-4d51-4742-a673-8b7299df6492")
    # package_ID="2acb2b77-b100-4beb-b072-d06bc3491a06"
    context = {
        'description' : obj.description,
        'pic' : obj.status,
    }

    return render(request, 'package/detail.html', context)