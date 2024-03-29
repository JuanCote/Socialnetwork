from django import forms
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension

from .models import Post, Profile


class Login(forms.ModelForm):
    password = forms.CharField(
        max_length=60,
        required=True,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                "class": "pl-3 h-12 rounded-md border-slate-500 border mb-3",
                "placeholder": "Password",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["email", "password"]
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email adress",
                    "class": "pl-3 h-12 rounded-md border-slate-500 border mb-3",
                }
            )
        }


class Register(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "rounded-md bg-slate-100 h-10 w-1/2 pl-3 border border-gray-300",
            }
        ),
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "bg-slate-100 ml-3 rounded-md pl-3 w-1/2 border-gray-300 border",
                "placeholder": "Surname",
            }
        ),
    )
    password = forms.CharField(
        min_length=6,
        max_length=30,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "mt-3 h-10 bg-slate-100 w-full rounded-md pl-3 border-gray-300 border",
                "placeholder": "New password",
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "mt-3 h-10 bg-slate-100 w-full rounded-md pl-3 border-gray-300 border",
                "placeholder": "Email adress",
            }
        )
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "password", "email"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            self.add_error(None, "Email address already exists")
        return email

    def clean_password(self):
        return make_password(self.cleaned_data["password"])

    def clean(self):
        try:
            last_id = User.objects.latest("id").id
        except:
            last_id = 0
        self.instance.username = last_id + 1


class PostForm(forms.ModelForm):
    content = forms.CharField(
        max_length=188,
        widget=forms.Textarea(
            attrs={
                "type": "text",
                "cols": "80",
                "class": "overflow-y-hidden resize-none w-full h-16 p-4 border-b rounded outline-none font-sans font-medium text-base",
                "placeholder": "What`s on your mind",
            }
        ),
    )
    image = forms.ImageField(
        required=False,
        validators=[validate_image_file_extension],
        widget=forms.FileInput(
            attrs={
                "class": "w-0.5 h-0.5 absolute opacity-0",
                "id": "file-input",
                "onChange": "handleImageUpload()",
            }
        ),
    )

    class Meta:
        model = Post
        fields = ["content", "image"]


class ProfileForm(forms.ModelForm):
    about_me = forms.CharField(
        min_length=2,
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "About me",
                "class": "rounded-md bg-slate-100 h-10 w-full pl-3 border border-gray-300",
            }
        ),
    )
    interested_in = forms.CharField(
        min_length=2,
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Interested in",
                "class": "rounded-md bg-slate-100 h-10 w-full pl-3 border border-gray-300",
            }
        ),
    )
    relationship_status = forms.CharField(
        min_length=2,
        max_length=23,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Relationship",
                "class": "rounded-md bg-slate-100 h-10 w-1/2 pl-3 border border-gray-300",
            }
        ),
    )
    looking_for = forms.CharField(
        min_length=2,
        max_length=23,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Looking for",
                "class": "rounded-md bg-slate-100 h-10 w-1/2 pl-3 border border-gray-300",
            }
        ),
    )
    sex = forms.CharField(
        min_length=2,
        max_length=10,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sex",
                "class": "rounded-md bg-slate-100 h-10 w-1/2 pl-3 border border-gray-300",
            }
        ),
    )
    birthday = forms.DateField(widget=forms.TextInput(attrs={'class': 'rounded-md bg-slate-100 h-10 w-1/2 pl-3 border border-gray-300', 'type':'date'}))
    hometown = forms.CharField(
        min_length=2,
        max_length=23,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Hometown",
                "class": "rounded-md bg-slate-100 h-10 w-full pl-3 border border-gray-300",
            }
        ),
    )

    class Meta:
        model = Profile
        fields = [
            "sex",
            "interested_in",
            "relationship_status",
            "looking_for",
            "birthday",
            "hometown",
            "about_me",
        ]


class EditAvaForm(forms.ModelForm):
    image = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={
                "id": "imageInput",
                "class": 'hidden'
            }
        ),
    )

    class Meta:
        model = Profile
        fields = ['avatar']

    def save(self):
        profile = self.instance
        profile.avatar = self.cleaned_data['image']
        profile.save()


    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.content_type.startswith('image'):
                raise forms.ValidationError('Empty image')
        return image
