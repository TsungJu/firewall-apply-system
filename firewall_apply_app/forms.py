from dataclasses import fields
from django import forms
from firewall_apply_app.models import FirewallApply

class FirewallApplyForm(forms.ModelForm):
    class Meta:
        model = FirewallApply
        fields = ("name",
        "phone_number",
        "email",
        "device_place_location",
        "source_ip_address",
        "destination_ip_address",
        "open_direction",
        "protocols",
        "ports",
        "reason",
        "apply_during_begin",
        "apply_during_end",
        "declare",)

    
