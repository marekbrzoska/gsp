from django import forms


class SuggestForm(forms.Form):
    so_far_numbers = forms.CharField()
    so_far_words = forms.CharField()
    next = forms.CharField()

    def clean(self):
        pass
