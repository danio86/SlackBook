from django.forms import ModelForm
from .models import Channel


class ChannelForm(ModelForm):
    class Meta:
        model = Channel
        fields = '__all__'

# this shows the model(Channel) i want to create a form for and the
# writable fields. Alternatively: ['body', 'title',...]
# These are Metadata from the Channel-Model
# the form itself is from Django
