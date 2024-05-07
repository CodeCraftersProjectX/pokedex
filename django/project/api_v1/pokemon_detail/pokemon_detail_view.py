from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated
from .pokemon_detail_serializer import PokemonDetailSerializer
from pokedex.models import Pokemon

# Usage APIView (自身でViewをカスタムする際はこれを継承すると良い)
class PokemonDetailView(APIView):
    # API_KEY認証
    permission_classes = [HasAPIKey | IsAuthenticated] 

    def get(self, request, number):  # URL パスから number を取得
        try:
            pokemon = Pokemon.objects.get(number=number)
            serializer = PokemonDetailSerializer(pokemon)
            return Response(serializer.data)
        except Pokemon.DoesNotExist:
            return Response({'error': 'Pokemon not found'}, status=404)
        
    def post(self, request, number, *args, **kwargs):
        try:
            pokemon = Pokemon.objects.get(number=number)
            serializer = PokemonDetailSerializer(pokemon, data=request.data)
        except Pokemon.DoesNotExist:
            return Response({'error': 'Pokemon not found'}, status=404)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

# Usage　RetrieveAPIView (GenericAPIView + RetrieveModelMixin) : 単体取得機能がすでに実装されている
class RetrievePokemonView(RetrieveAPIView):
    # 公式Doc見ると、ここに queryset や serializer_class を定義しているが、しなくても動いた

    # pkでなくnumberを指定しているため、retrieveメソッドをoverride
    def retrieve(self, request, number):        
        # 以下の便利関数があるので使ってみた。ただし、レスポンスが {"detail":"見つかりませんでした。"} になる
        pokemon = get_object_or_404(Pokemon, number=number)
         # シリアライズ
        serializer = PokemonDetailSerializer(pokemon)
        return Response(serializer.data)
