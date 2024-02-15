import requests
from django.contrib.auth.models import User
import json
from django.test import Client
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth.hashers import make_password, check_password

class authentication_middleware():
    def __init__(self, get_response):
        self.get_response = get_response
        print("one time initialization")

    def __call__(self, request):
        """ by default django provide HTTP request authorization 
        in request.META not in request.headers"""
        if 'HTTP_AUTHORIZATION' not in request.META and \
            'x-user-name' in request.headers:
            user_name = request.headers['x-user-name']
            if User.objects.filter(username=user_name).exists():
                user_obj = User.objects.filter(username=user_name).first()
                # Refresh token generate refresh and access tokens
                refresh = RefreshToken.for_user(user_obj)  
                access_token = str(refresh.access_token)
                request.META['HTTP_AUTHORIZATION'] = f"Bearer {access_token}"
        response = self.get_response(request)
        return response