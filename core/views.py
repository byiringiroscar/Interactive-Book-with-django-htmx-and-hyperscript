from django.shortcuts import render
from core.forms import BookForm

# Create your views here.
def index(request):
    context = {
        'form': BookForm()
    }
    return render(request, 'index.html', context)