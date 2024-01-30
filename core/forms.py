from django.forms import ModelForm
from .models import Room, Message

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' #Or ['name', 'description']
        

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__' #Or ['name', 'description']
        
