from Browse.models import Items
from django import forms


class ItemUploadForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ['item_name', 'item_desc', 'min_price', 'buy_now_price', 'expiration', 'item_logo']