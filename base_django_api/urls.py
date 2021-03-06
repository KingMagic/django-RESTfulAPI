from base.views import UploadFile, TestView, BeginCelery, ConfDictViewset, ConfDictSearchView, UploadLocalFile
from user.views import LoginView, UserViewset, UserInfo, AuthViewset, WeChatUpdateUserViewset, WeChatMiniLoginView, WeChatAppLoginView, MemberViewset
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# 新版swagger
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Django RESTfulAPI",
        default_version='v2.2',
        description="Ddescription",
        terms_of_service="https://blog.csdn.net/haeasringnar",
        contact=openapi.Contact(email="aeasringnar@163.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# 使用 viewset 路由管理
router = DefaultRouter()
# 账号管理
router.register(r'user', UserViewset, base_name='账号管理')
# 普通用户管理
router.register(r'member', MemberViewset, base_name='用户管理')
# 权限管理
router.register(r'auth', AuthViewset, base_name='权限管理')
# 系统字典管理
router.register(r'confdict', ConfDictViewset, base_name='系统字典管理')
# 全文检索路由 检索系统字典
router.register(r'searchdict', ConfDictSearchView, base_name='全文检索系统字典')
# 修改用户个人信息
router.register(r'updateuser', WeChatUpdateUserViewset, basename='修改个人信息')


urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
    path('adminlogin/', LoginView.as_view(), name='后台登录'),
    path('wxminilogin/', WeChatMiniLoginView.as_view(), name='微信小程序登录'),
    path('wxapplogin/', WeChatAppLoginView.as_view(), name='微信APP三方登录'),
    path('uploadfile/', UploadLocalFile.as_view(), name='文件上传'), # UploadFile UploadLocalFile 
    path('test/', TestView.as_view(), name='测试接口'),
    path('userinfo/', UserInfo.as_view(), name='个人信息'),
    path('celery/', BeginCelery.as_view(), name='celery测试'),
]
