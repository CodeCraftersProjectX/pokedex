from pokedex.models import Pokemon
from rest_framework import serializers

# レスポンスは Pokemon_Model (の一部)に他ならないため、ModelSerializer を継承して実装
class PokemonListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Pokemon
        fields = (
            'number',
            'name',
            'types',
            'height',
            'weight',
            'description',
            )
