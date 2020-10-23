from django import forms

class JatakaForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50, widget=forms.TextInput(attrs={'placeholder':'Achyutha'}), required=False)
    birth_place = forms.CharField(label='Place of Birth', max_length=50, widget=forms.TextInput(attrs={'placeholder':'Bengaluru'}))
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'27.6.1990'}))
    time_of_birth = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'15.35'}))
    latitude = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder':'22.34'}))
    longitude = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder':'88.24'}))
