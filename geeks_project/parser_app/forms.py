from django import forms
from . import models, parser

class ParserForm(forms.Form):
    MEDIA_CHOICES = (("house.kg", 'house.kg'),)
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ['media_type']

    def parser_data(self):
        if self.data['media_type'] == 'house.kg':
            house_parser = parser.parser_houses()
            for item in house_parser:
                models.HouseModel.objects.create(**item)