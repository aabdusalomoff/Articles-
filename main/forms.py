from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.FileField()
    category = forms.IntegerField()


    
    def clean(self):
        return super().clean()
    
