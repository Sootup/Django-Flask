from rest_framework import serializers
from .models import user
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ("title","context","cat")
    













# class UserSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=250)
#     context = serializers.CharField()
#     time_created = serializers.DateTimeField(read_only=True)
#     date_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return user.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.context = validated_data.get('title',instance.context)
#         instance.date_update = validated_data.get('title',instance.date_update)
#         instance.is_published = validated_data.get('title',instance.is_published)
#         instance.cat_id = validated_data.get('title',instance.cat_id)
#         return instance

# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = user
#         fields = ('title','cat_id')

# class Usermodel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content



# class UserSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()

# def encode():
#     model = Usermodel('title', 'content: rist_content')
#     model_sr = UserSerializer(model)
#     print(model_sr.data, type(model_sr))
#     json = JSONRenderer().render(model_sr.data)
#     print(json)


# def decode():
#     stream = io.BytesIO(b'{"title":"first_title", "content: rist_content"}')
#     data = JSONParser().parse(stream)
#     serializer = UserSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)