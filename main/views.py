from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'project_name' : 'Warung Anomali',
        'npm' : '2306123456',
        'name': 'Pak Bepe',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)