from django.forms import ModelForm
from .models import Room, Message, User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' 
        exclude = ['host', 'participants']
        

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__' #Or ['name', 'description']
        

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']