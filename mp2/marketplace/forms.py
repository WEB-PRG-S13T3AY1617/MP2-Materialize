from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from marketplace.models import Post, Offer


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
    type = forms.ChoiceField(choices=Post.CHOICES, required=True)
    quantity = forms.IntegerField(required=True, initial='1', min_value=1)

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
        post = super(PostForm, self).save(commit=False)
        post.name = self.cleaned_data['name']
        post.condition = self.cleaned_data['condition']
        post.type = self.cleaned_data['type']
        post.quantity = self.cleaned_data['quantity']

        if commit:
            post.save()

        return post


class OfferForm(forms.ModelForm):
    type = forms.ChoiceField(choices=Offer.CHOICES, required=True)

    class Meta:
        model = Offer
        fields = (
            'type',
            'amount',
            'secondhand',
        )

    def save(self, commit=True):
        offer = super(OfferForm, self).save(commit=False)
        offer.type = self.cleaned_data['type']
        offer.amount = self.cleaned_data['amount']
        offer.secondhand = self.cleaned_data['secondhand']

        if commit:
            offer.save()

        return offer
#
#
# class AcceptRejectForm(forms.ModelForm):
#     reason = forms.CharField(required=True, max_length=255)
#
#     class Meta:
#         model = Offer
#         fields = (
#             'reason',
#             'approve_reject',
#         )
#
#     def save(self, commit=True):
#         offer = super(AcceptRejectForm, self).save(commit=False)
#         offer.reason = self.cleaned_data['reason']
#         offer.approve_reject = self.cleaned_data['approve_reject']
#
#         if commit:
#             offer.save()
#
#         return offer
