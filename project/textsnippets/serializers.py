
from rest_framework import serializers
from textsnippets.models import *
from authentication.models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

class TextsnippetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textsnippet
        fields = '__all__'
