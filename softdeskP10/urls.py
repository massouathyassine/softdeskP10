"""softdeskP10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from userAccount.views import UserAccountViewSet
from helpdesk.views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet


account_router = DefaultRouter()
account_router.register(r'signup', UserAccountViewSet)

project_router = routers.SimpleRouter()
project_router.register(r'projects', ProjectViewSet, basename='project')

project_router_nested = routers.NestedSimpleRouter(project_router, r'projects', lookup='project')
project_router_nested.register(r'users', ContributorViewSet, basename='user')
project_router_nested.register(r'issues', IssueViewSet, basename='issue')

issue_router_nested = routers.NestedSimpleRouter(project_router_nested, r'issues', lookup='issue')
issue_router_nested.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(account_router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(project_router.urls)),
    path('', include(project_router_nested.urls), name='project'),
    path('', include(issue_router_nested.urls), name='issue'),
]
