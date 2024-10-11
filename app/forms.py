from django import forms
from .models import Detail


class UserForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['firstname','surname','lastname','skill1','skill2','skill3','profile_img','background_img','profession','overview','contact_number','email','address','portfolio','role1','role1_info','role2','role2_info','role3','role3_info']
