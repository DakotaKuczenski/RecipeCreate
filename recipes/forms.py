from django import forms
from .models import Post
from django.forms import formset_factory

class ImageUploadForm(forms.ModelForm):
    class meta:
        model = Post
        file = ['recipe_image']


#adding this class. for dynamic
class recipeIngredients(forms.ModelForm):
    name = forms.CharField(
        label='Ingredient name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Ingredient Name here'
        })
    )
IngredientsFormset = formset_factory(recipeIngredients, extra=1)
