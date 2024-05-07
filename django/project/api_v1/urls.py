from django.urls import path
from rest_framework.authtoken import views as auth_views

from .pokemon_list.pokemon_list_view import PokemonListView
from .pokemon_detail.pokemon_detail_view import PokemonDetailView, RetrievePokemonView

app_name = 'api_v1'
urlpatterns = [
    # 一覧取得API
    # get も post もエンドポイントは同じにしている
    path('pokemon/', PokemonListView.as_view(), name='pokemon_list'),
    
    # 詳細取得API
    # 以下のように書くと、pokemon/1/ のように指定されたpathから number = 1 (int型)としてViewに渡す
    # NOTE: 詳細取得APIでid等を指定する際はリクパラでなく、pathの末尾に指定する方が良いらしい
    path('pokemon/<int:number>/', PokemonDetailView.as_view(), name='pokemon_detail'),

    # 詳細取得API (Retrieve Mixin ver.)
    path('pokemon/retrieve/<int:number>/', RetrievePokemonView.as_view(), name='retrieve_pokemon'),


    # Token発行
    path('authorize/', auth_views.obtain_auth_token, name='obtain_auth_token'),
]