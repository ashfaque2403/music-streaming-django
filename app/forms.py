# from django  import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import Comment

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
















# class SignupForm(forms.ModelForm):
#     password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)

#     class Meta():
#         model=UserProfile
#         fields=('username','email','password','pro_image')

        
# class UserRegistrationForm(forms.ModelForm):
#     profile_image=forms.ImageField(required=False)

#     class Meta:
#         model=User
#         fields=('username','email','password','profile_image')

#     def save(self, comit=True):
#         user=super().save()
        
#         if self.cleaned_data['profile_image']:
#             profile_image=self.cleaned_data['profile_image']
#             user_profile=UserProfile(user=user,profile_image=profile_image)
#             if comit:
#                 user.save()
#                 user_profile.save()
#             return user,user_profile
#         if comit:
#             user.save()
#         return user
