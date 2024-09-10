from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'project_name' : 'Warung Anomali',
        'npm' : '2306241713',
        'name': 'Andi Muhammad Adlyn Fakhreyza Khairi Putra',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)