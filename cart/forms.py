"""
    class CartAddProductForm - форма которая будет добавлять продукты в корзину
    quantity - позволяет пользователю выбрать количество между 1-20. TypedChoiceField с coerce=int испольхывается
     для преобразования ввода в целое число.
     update - позволяет указать, следует ли добавлять сумму к любому существующему значению в корзине для данного
     продукта (False) или если существующее значение должно быть обновлено с заданным значением (True).
     Для этого поля используется графический элемент HiddenInput, поскольку не требуется показывать его пользователю.

"""

from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
