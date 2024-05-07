# from rest_framework.authentication import TokenAuthentication

# # POSTリクエストのみ、トークンを要求する
# class CustomTokenAuthentication(TokenAuthentication):
#     def authenticate(self, request):
#         if request.method == 'POST':
#             return super().authenticate(request)
#         else:
#             return None  # GETリクエストの場合はトークン認証を行わない