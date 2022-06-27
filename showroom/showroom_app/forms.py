from django import forms
from . import models


class StaffForm(forms.ModelForm):
    class Meta:
        model = models.Staff
        fields = "__all__"
        labels = {
            "Staffname": "Name",
            "Staffid": "ID",
            "PanCard": "PAN Card",
            "AdharcardNo": "Aadhar Card",
            "Phno": "Phone",
            'pwd': "Password"
        }
        widgets = {
            "pwd": forms.PasswordInput()
        }

    def clean_title(self, *args, **kwargs):
        id = self.cleaned_data.get("Staffid")
        print(id)
        qs = models.Staff.objects.filter(Staffid=id)
        if qs.exists():
            raise forms.ValidationError("this id is present")
        return id


class VehicleForm(forms.Form):
    VehicleType = forms.CharField(label="Vehicle Type", max_length=20)
    VehicleNo = forms.IntegerField(label="Vehicle Number")
    Company = forms.CharField(label="Company", max_length=20)


class StockForm(forms.Form):
    Stock = forms.IntegerField(label="Stock")
    VehicleNo = forms.IntegerField(label="Vehicle Number")
    StockID = forms.IntegerField(label="Stock ID")


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = "__all__"
        # ["Staffname","Staffid","Address","PanCard","AdharcardNo","Phno"]
        labels = {
            "Custname": "Name",
            "PanCard": "PAN Card",
            "AdharcardNo": "Aadhar Card",
            "Phno": "Phone",
            "pwd": "Password"
        }
        widgets = {
            "pwd": forms.PasswordInput()
        }
        exclude = ["Custid"]

    def clean_title(self, *args, **kwargs):
        id = self.cleaned_data.get("Custid")
        print(id)
        qs = models.Staff.objects.filter(Custid=id)
        if qs.exists():
            raise forms.ValidationError("this id is present")
        return id


class LoginForm(forms.Form):
    mail = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'username'}))
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'password'}))


class Feedback_form(forms.ModelForm):
    class Meta:
        model = models.feedback
        fields = "__all__"
