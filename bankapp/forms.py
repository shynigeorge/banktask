
from django import forms

from .models import Register, City



class AccountForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput)
    dob = forms.DateField(widget=forms.DateInput)
    age = forms.CharField(widget=forms.TextInput)
    CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = forms.CharField(widget=forms.RadioSelect(choices=CHOICES))

    mobile = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    address = forms.CharField(widget=forms.TextInput)






    DEMO = [
        ('', 'Select Type'),
        ('Savings Account', 'Savings Account'),
        ('Current Account', 'Current Account'),
    ]
    account = forms.CharField(widget=forms.Select(choices=DEMO))
    METERIAL = [
        ('Debit Card', 'Debit Card'),
        ('Credit Card', 'Credit Card'),
        ('Cheque Book', 'Cheque Book'),
    ]
    material = forms.CharField(widget=forms.RadioSelect(choices=METERIAL))

    class Meta:
        model = Register
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['city'].queryset = City.objects.filter(district_id=district_id).all()
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.district.city_set.order_by('name')


