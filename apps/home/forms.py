# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from .models import Cases


class CasesForm(forms.ModelForm):
    casetype = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "casetype",
                "class": "form-control"
            }
        ))
    fir = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "fir",
                "class": "form-control"
            }
        ))
    ps = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "ps",
                "class": "form-control"
            }
        ))
    telco = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "telco",
                "class": "form-control"
            }
        ))
    voip = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "voip",
                "class": "form-control"
            }
        ))
    complaintcaste = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "complaintcaste",
                "class": "form-control"
            }
        ))
    modusoperandus = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "modusoperandus",
                "class": "form-control"
            }
        ))
    casetitle = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "casetitle",
                "class": "form-control"
            }
        ))
    casedate = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "casedate",
                "class": "form-control"
            }
        ))
    region = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "region",
                "class": "form-control"
            }
        ))
    internationalno = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "internationalno",
                "class": "form-control"
            }
        ))
    coplaintname = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "coplaintname",
                "class": "form-control"
            }
        ))
    profession = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "profession",
                "class": "form-control"
            }
        ))
    incidentdate = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "incidentdate",
                "class": "form-control"
            }
        ))
    firreference = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "firreference",
                "class": "form-control"
            }
        ))
    us = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "us",
                "class": "form-control"
            }
        ))
    localno = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "localno",
                "class": "form-control"
            }
        ))
    country = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "country",
                "class": "form-control"
            }
        ))
    complaintno = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "complaintno",
                "class": "form-control"
            }
        ))
    groupclaim = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "groupclaim",
                "class": "form-control"
            }
        ))
    incidenttime = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "incidenttime",
                "class": "form-control"
            }
        ))
    incident_ps_jurisdiction = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "incident_ps_jurisdiction",
                "class": "form-control"
            }
        ))
    demand_amount = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "demand_amount",
                "class": "form-control"
            }
        ))
    victim_reference = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "victim_reference",
                "class": "form-control"
            }
        ))
    victim = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "victim",
                "class": "form-control"
            }
        ))
    io = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "io",
                "class": "form-control"
            }
        ))
    remarks = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "remarks",
                "class": "form-control"
            }
        ))
    incident_place = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "incident_place",
                "class": "form-control"
            }
        ))


    class Meta:
        model = Cases
        fields = ('casetype', 'fir', 'ps', 'telco','voip', 'complaintcaste', 'modusoperandus', 
            'casetitle','casedate', 'region', 'internationalno', 'coplaintname','profession',
             'incidentdate', 'firreference', 'us','localno', 'country', 'complaintno', 'groupclaim',
             'incidenttime',"incident_ps_jurisdiction","demand_amount","victim_reference","victim","io","remarks","incident_place")
        
