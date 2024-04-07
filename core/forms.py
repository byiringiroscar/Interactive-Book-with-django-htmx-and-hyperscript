from django import forms
from core.models import Book



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author')

    
    def clean_name(self):
        name = self.changed_data['name']
        if name.startswith('a'):
            raise forms.ValidationError("Error: we don't want people whose name starts with a")
        
        return name
