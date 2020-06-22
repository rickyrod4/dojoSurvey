from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'name' not in request.session:
        request.session['name'] = 'new user'


    context = {
        'name' : request.session['name'],
        'location' : request.session['location'],
        'language' : request.session['language'],
        'comment' : request.session['comment']
    }
    print(context)
    return render(request, 'index.html', context)

def result(request):
    #print(request.POST)

    request.session['name'] = request.POST['name'],
    request.session['location'] = request.POST['location'],
    request.session['language'] = request.POST['language'],
    request.session['comment'] = request.POST['comment'],
    
    return redirect('/')
    #return render(request, 'result.html', context)

def reset(request):
    del request.session['context']
    return redirect('/')