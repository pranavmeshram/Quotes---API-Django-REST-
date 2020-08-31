from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from quotes_app.models import Quotes

class QuotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = ("id", "sr_lang", "en_lang", "author", "source", "rating")
