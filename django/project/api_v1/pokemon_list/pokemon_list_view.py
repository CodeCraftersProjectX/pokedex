from pokedex.models import Pokemon
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
# from rest_framework.authentication import TokenAuthentication
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated
from .pokemon_list_serializer import PokemonListSerializer

class PokemonListView(APIView):
    # pagination
    pagination_class = PageNumberPagination
    # API_KEY認証
    permission_classes = [HasAPIKey | IsAuthenticated] 

    def get(self, request):
        try:
            pokemons = Pokemon.objects.all()

            # ページサイズをリクエストパラメータから取得する
            per_page = request.query_params.get('per_page', 10)

            # ページネーションを適用
            paginator = self.pagination_class()
            paginator.page_size = per_page  # ページサイズを設定
            result_page = paginator.paginate_queryset(pokemons, request)

            serializer = PokemonListSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except:
            return Response({'error': 'Pokemon not found'}, status=404)
    
    def post(self, request, *args, **kwargs):
        serializer = PokemonListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
