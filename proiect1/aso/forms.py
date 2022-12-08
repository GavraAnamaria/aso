
from .models import Mesaj
from django.forms import ModelForm
##https://www.geeksforgeeks.org/python-uploading-images-in-django/

class FormMsg(ModelForm):
    class Meta:
        model = Mesaj
        fields = ['msg_text', 'msg_image',]

