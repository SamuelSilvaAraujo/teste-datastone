import requests
from rest_framework import serializers

COIN_CHOICES = (
    ("BRL", "Real Brasileiro"),
    ("USD", "Dólar Americano"),
    ("EUR", "Euro"),
    ("BTC", "Bitcoin"),
    ("ETH", "Ether"),
)


class ConverterSerializer(serializers.Serializer):
    value = serializers.DecimalField(max_digits=16, decimal_places=2)
    from_coin = serializers.ChoiceField(choices=COIN_CHOICES)
    to_coin = serializers.ChoiceField(choices=COIN_CHOICES)
    result = serializers.SerializerMethodField()

    def validate(self, attrs):
        from_coin = attrs["from_coin"]
        to_coin = attrs["to_coin"]

        if from_coin == to_coin:
            raise serializers.ValidationError(
                {"from_coin": "Moedas não podem ser iguais!"}
            )
        return super().validate(attrs)

    def get_result(self, obj):
        from_coin = obj.get("from_coin")
        to_coin = obj.get("to_coin")
        url = f"https://economia.awesomeapi.com.br/last/{to_coin}-{from_coin}"
        r = requests.get(url=url)
        data = r.json().get(f"{to_coin}{from_coin}", None)
        if data:
            return data["high"]
        else:
            return None
