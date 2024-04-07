from django.shortcuts import render
from core.forms import BookForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'form': BookForm()}
            return render(request, 'partials/bookform.html',context)
        context = {'form': form}
        return render(request, 'partials/bookform.html',context)
    context = {
        'form': BookForm()
    }
    return render(request, 'index.html', context)