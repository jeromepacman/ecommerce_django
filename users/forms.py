from django import forms
from django.contrib.auth import password_validation,authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, \
    SetPasswordForm, AuthenticationForm
from users.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages


class UserRegisterForm(UserCreationForm):
    """
        A form to creates a user
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Email *'}))
    password1 = forms.CharField(strip=False,
                                widget=forms.PasswordInput(
                                    attrs={'autocomplete': 'current-password', "class": 'form-control',
                                           'placeholder': 'Mot de passe (8 caractères mini) *'}))
    password2 = forms.CharField(strip=False,
                                widget=forms.PasswordInput(
                                    attrs={'autocomplete': 'new-password', "class": 'form-control',
                                           'placeholder': 'confirmation du mot de passe *'}))
    mobile_no = forms.CharField(min_length=12, max_length=15, required=False, widget=forms.TextInput(
        attrs={"class": 'form-control', 'placeholder': 'tel mobile'}))
    alt_mobile_no = forms.CharField(min_length=12, max_length=15, required=False, widget=forms.TextInput(
        attrs={"class": 'form-control', 'placeholder': 'autre tel'}))

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "mobile_no", "alt_mobile_no"]


class LoginForm(AuthenticationForm):
    """
        A form that allows user to login with correct username and password.
    """
    error_messages = {
        "Données incompatibles":
            "Entrez un identifiant et son mot de passe valide, merci."
        ,
        "inactive": "Ce compte n'est pas actif.",
    }

    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Email *'}))
    password = forms.CharField(strip=False,
                               widget=forms.PasswordInput(
                                   attrs={'autocomplete': 'current-password', "class": 'form-control',
                                          'placeholder': 'mot de passe *'}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                messages.error(self.request, "Saisie sans résultat")
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30,
                                 widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Prénom',
                                                               }))
    last_name = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Nom',
                                                              }))
    username = forms.CharField(max_length=150,
                               widget=forms.TextInput(
                                   attrs={"class": 'form-control', 'placeholder': 'Email'}))
    mobile_no = forms.CharField(min_length=12, max_length=15, required=False, widget=forms.TextInput(
        attrs={"class": 'form-control', 'placeholder': 'tel mobile'}))
    alt_mobile_no = forms.CharField(min_length=12, max_length=15, required=False, widget=forms.TextInput(
        attrs={"class": 'form-control', 'placeholder': 'Autre tel'}))
    address_one = forms.CharField(max_length=250, required=False, widget=forms.TextInput(
        attrs={"class": 'form-control', 'placeholder': 'Adresse', 'label': 'Address 1'}))
    address_two = forms.CharField(max_length=250, required=False, widget=forms.TextInput(
        attrs={"class": 'form-control', 'placeholder': 'Ville', 'label': 'Address 2'}))
    zipcode = forms.CharField(max_length=25, required=False, widget=forms.TextInput(
        attrs={"class": 'form-control', 'placeholder': 'Code postal'}))


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, "placeholder": "Ancien mot de passe",
                   'class': 'form-control'}
        ),
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "placeholder": "Nouveau mot de passe", 'class': 'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "placeholder": "Confirmer nouveau mot de passe", 'class': 'form-control'}),
    )


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control', 'placeholder': 'Email'})
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        messages.error(request="Entrez un email valide")
        raise ValidationError("Entrez un email valide")


class ResetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'mot de passe'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Confirmer mot de passe'}),
    )