from django import forms

class msgForm(forms.Form):
    msg= forms.CharField(widget=forms.Textarea(attrs={
        'rows' : 4,
        'class' : 'answers',
        }))
    emisor= forms.CharField(label="emisor", max_length=256,required=False)
    receptor= forms.CharField(label="recepto",max_length=256,required=True)
    leido= forms.BooleanField(label="leido?",required=False)