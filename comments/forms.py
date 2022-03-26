from .models import Comment
from django.forms import ModelForm

class FormComment(ModelForm):
    def clean(self):
        data = self.cleaned_data

        name = data.get('name', None)
        email = data.get('email', None)
        text  = data.get('text', None)

        if len(name) < 4:
            self.add_error('name', 'Coloque um Nome certo e para de Macacada! 💀')

        if name == None or email == None or text == None:
            self.add_error('name', 'Complete os campos abaixo antes de Comentar!! 💀💀')

    class Meta:
        model = Comment
        fields = ('name', 'email', 'text',)