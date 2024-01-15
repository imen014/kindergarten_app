from django.forms import ModelForm
from django import forms
from kids_schools_management.models import Kids_school



class Kids_schoolForm(ModelForm):
    class Meta:
        model = Kids_school
        fields = ['school_name','school_location', 'school_owner', 'manager_email', 'manager_tel']
        labels = {
            'school_name':'school name',
            'school_location':'school location',
            'school_owner':'school owner',
            'manager_email':'manager email',
            'manager_tel':'manager tel',

        }


class Updater_school_instance(ModelForm):
    class Meta:
        model = Kids_school
        fields = ['school_name','school_location', 'school_owner', 'manager_email', 'manager_tel']
        labels = {
            'school_name':'school name',
            'school_location':'school location',
            'school_owner':'school owner',
            'manager_email':'manager email',
            'manager_tel':'manager tel',

        }
    
