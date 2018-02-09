from django.shortcuts import render

from .forms import Contact


def index(request):
    success = False
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            form.send_mail()
            form = Contact()
            success = True
    else:
        form = Contact()
    context = {
        'form': form,
        'success': success,
    }
    return render(request, 'index.html', context)
