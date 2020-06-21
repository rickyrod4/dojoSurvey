from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'name' not in request.session:
        request.session['name'] = 'new user'
    return render(request, 'index.html')

def result(request):
    print(request.POST)
    context = {
        "name" : request.POST['name'],
        'location' : request.POST['location'],
        'language' : request.POST['language'],
        "comment" : request.POST['comment']
    }
    
    return render(request, 'result.html', context)