from django import forms

from .models import Article

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.FileField()
    category = forms.IntegerField()


    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title.istitle():
            raise forms.ValidationError("Title katta harflarda bo'lishi kerak")
        

        return title
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description)<20:
            raise forms.ValidationError("Uzunlik yetarli emas ")
    
        return description
    

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','description','image','category','author']