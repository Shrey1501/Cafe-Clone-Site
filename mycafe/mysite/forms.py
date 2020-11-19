from django import forms
from mysite.models import ReserveInfo

class ReserveInfoForm(forms.ModelForm):

    class Meta():
        model = ReserveInfo
        fields = ('Name','Email','People')

        
