from django.shortcuts import render
from core.forms import BookForm
from core.models import Book

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'form': BookForm()}
            response = render(request, 'partials/bookform.html',context)
            response['HX-Trigger'] = 'bookAdded'
            return response
        context = {'form': form}
        return render(request, 'partials/bookform.html',context)
    context = {
        'form': BookForm(),
        'books': Book.objects.all()
    }
    return render(request, 'index.html', context)