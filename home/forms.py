from django.forms import ModelForm
from .models import Comment
    

        
        
class MyBaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
            
class CommentForm(MyBaseForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']
        labels = {'name': "Your name", 'comment': "Comment"}
        #fields = ['name', 'email', 'subject', 'comment']
        #labels = {'name': "Your name", 'Your Email': "email", 'Subject': "subject", 'comment': "Comment"}
