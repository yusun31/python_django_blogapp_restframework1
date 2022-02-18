
#### django REST framework 설치 using pip
```
pip install djangorestframework
```

#### settings.py INSTALLED APPS 에 추가해야함
```
INSTALLED_APPS = [

    'rest_framework',
]
```

* 전체목록조회 GET http://localhost:8000/blog/posts
* 1개 조회 GET http://localhost:8000/blog/posts/1
* 등록 POST http://localhost:8000/blog/posts/  ( / 슬래쉬 꼭 )
* 수정 PUT http://localhost:8000/blog/posts/1/  ( / 슬래쉬 꼭 )
* 삭제 DELETE http://localhost:8000/blog/posts/1/ ( / 슬래쉬 꼭 )


#### django REST framework 가 제공하는 TokenAuthentication을 사용해서 인증을 처리

##### 로그인과정 (token authentication)
* 1 화면에서 사용자가 username, password를 입력하서 서버로 보낸다.
* 2 username, password 가 맞다면 고유한 TOKEN을 발행하고 토큰을 response로 보낸다
* 3 다른 API를 사용할 때마다 header에 TOKEN을 같이 서버에 보낸다.
* 4 서버는 TOKEN 을 확인해서 token 이 valid 한지 확인한 뒤 response를 보낸다.

#### settings.py INSTALLED APPS 에 추가해야함
```
INSTALLED_APPS = [
	...
    'rest_framework.authtoken'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',)
}
```

#### settings.py 를 수정한 후에는 migrate 를 실행한다
```
python manage.py migrate
```

#### blog/views.py
```
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    #email = request.data.get('email')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)

    # 여기서 authenticate로 유저 validate
    user = authenticate(username=username, password=password)
    print('>>>> user ', user)

    if not user:
        return Response({'error': 'Invalid credentials'}, status=HTTP_404_NOT_FOUND)

    # user 로 토큰 발행
    token, _ = Token.objects.get_or_create(user=user)

    return Response({'token': token.key}, status=HTTP_200_OK)
```

####  blog/urls.py
```
urlpatterns = [
	path('api/login/', views.login, name='login')     # 추가!!
]
```

#####  API를 사용할 때마다 header에
```
 Authorization : Token 44ab7ccb9...
```
