from rest_framework import serializers

#import the todo  data model
from .models import Todo

#serializers convert the model into JSON 
class TodoSerializers(serializers.ModelSerializer):
    #create a meta class
    class Meta:
        model =Todo
        fields = ('id','title','description','completed')