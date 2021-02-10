"""
class Author(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField()

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=100)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} | {self.author}"
"""

from django import forms
from recipe_app.models import Author


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=40)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=100)
    instructions = forms.CharField(widget=forms.Textarea)


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name',
            'bio',
            'user',
        ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)
