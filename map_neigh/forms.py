from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserModel, Buildings, Announcement
from django.contrib.gis import forms

class NewUserForm(UserCreationForm):

    username = forms.CharField(label='Nazwa użytkownika', max_length=50)
    email = forms.CharField(label='Email', max_length=100)
    district = forms.ChoiceField(widget=forms.RadioSelect, choices=CustomUserModel.district_choices)
    address = forms.IntegerField(label='Adres', widget=forms.HiddenInput())
    password1 = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórnie wprowadź hasło', widget=forms.PasswordInput)

    class Meta(forms.Form):
        model = CustomUserModel
        fields = ('username', 'email', 'district', 'address', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.district = self.cleaned_data['district']
        user.address = Buildings.objects.get(id = self.cleaned_data['address'])
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()
        return user

class NewAnnouncementForm(forms.Form):

    text = forms.CharField(label='Treść ogłoszenia', max_length=1500)
    anouncement_type = forms.ChoiceField(widget=forms.RadioSelect, choices=Announcement.announcement_types)
    #user_name dodac do views przed savem i dodac w save (?)
    price = forms.DecimalField(label='Podaj oczekiwaną cenę, w przypadku darmowego ogłoszenia wpisz 0')

    class Meta(forms.Form):
        model = Announcement
        fields = ('text', 'announcement_type', 'user_name', 'date', 'price', 'building_id')

    def save(self, commit=True):
        announcement = super(NewAnnouncementForm, self).save(commit=False)
        announcement.text = self.cleaned_data['text']
        announcement.announcement_type = self.cleaned_data['announcement_type']
        announcement.price = self.cleaned_data['price']

        if commit:
            announcement.save()
        return announcement
