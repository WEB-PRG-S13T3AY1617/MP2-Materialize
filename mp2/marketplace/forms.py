from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from marketplace.models import Post


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    degree_or_office = forms.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'degree_or_office',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.degree_or_office = self.cleaned_data['degree_or_office']

        if commit:
            user.save()

        return user


class PostForm(forms.ModelForm):
    name = forms.CharField(required=True)
    condition = forms.CharField(required=True)
    type = forms.CharField(required=True)
    quantity = forms.IntegerField(required=True, min_value=1)

    class Meta:
        model = Post
        fields = (
            'image',
            'name',
            'condition',
            'quantity',
            'type',
            'course',
            'tags',
        )

    def save(self, commit=True):
        post = self.save(commit=False)
        post.name = self.cleaned_data['name']
        post.condition = self.cleaned_data['condition']
        post.type = self.cleaned_data['type']
        post.quantity = self.cleaned_data['quantity']

        if commit:
            post.save()

        return post
