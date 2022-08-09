import django.forms as forms
from .models import Note
from django.contrib.auth.models import User

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'message']


class ShareForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ShareForm, self).__init__(*args, **kwargs)
        self.fields['shared_with'].queryset = self.fields['shared_with'].queryset.exclude(username='admin')
        self.fields['shared_with'].queryset = self.fields['shared_with'].queryset.exclude(username=user)

    class Meta:
        model = Note
        fields = ['shared_with']
        labels = {
            'shared_with': 'Select users to share this note:'
        }

# class ShareForm(forms.ModelForm):
#     class Meta:
#         model = Note
#         fields = ['shared_with']

# def filter_out_current_user(request):
#     users = [(None, '------')]
#     for u in User.objects.all().exclude(id=request.user):
#         users.append((u, u.username))
#     return users
#
# class NoteForm(forms.Form):
#     title = forms.CharField(max_length=140, required=True)
#     message = forms.CharField(max_length=500, required=True)
#     shared_with = forms.ChoiceField(choices=filter_out_current_user())

# class NoteForm(forms.ModelForm):
#     # def __init__(self, **kwargs):
#     #     user = kwargs['instance'].creator
#     #     super(NoteForm, self).__init__(**kwargs)
#     #     self.fields['shared_with'].queryset = User.objects.exclude(user)
#     #     shared_with = forms.ModelChoiceField(queryset=User.objects.exclude(user), widget=forms.Select, required=False)
#     class Meta:
#         model = Note
#         fields = ['title', 'message', 'shared_with']
#         field_classes = {
#             'shared_with': SharedWithFormField,
#         }
#
# class SharedWithFormField(forms.Form):

# class NoteForm(forms.ModelForm):
#     def __init__(self, request, **kwargs):
#         user = None
#         if hasattr(request, 'GET'):
#             user = request.GET.get('user')
#         super(NoteForm, self).__init__(**kwargs)
#         self.fields['shared_with'].queryset = User.objects.exclude(id=user)
#     class Meta:
#         model = Note
#         fields = ['title', 'message', 'shared_with']