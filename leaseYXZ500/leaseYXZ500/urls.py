"""
URL configuration for leaseYXZ500 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.urls import  re_path
from Z500 import views
from Z500.tools import viewss
from . import  testdb


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^ifc/index$', views.index),
    re_path(r'^approve/pro/add$', viewss.testApproveFlow),
    re_path(r'^approve/', viewss.testApprove),
    re_path(r'^paymentApprove/pro/add$', viewss.testPaymentApproveFlow),
    re_path(r'^paymentApprove/', viewss.testPaymentApprove),

    re_path(r'^data/pro/add$', viewss.test_add_pro),
    re_path(r'^data/', viewss.testMakeData),
    re_path('^demo$', views.demo),
    re_path(r'^ifc/', viewss.test_qq),
    re_path(r'^contract/pro/add$', viewss.testContractAdd),
    re_path(r'^contract/', viewss.testContract),
    re_path(r'^middleCode/pro/add$', viewss.testMiddleCodeQuery),
    re_path(r'^middleCode/', viewss.testMiddleCode),
    re_path(r'^direct/', viewss.testDirect),
    re_path(r'^payment/pro/add$', viewss.testPaymentAdd),
    re_path(r'^payment/', viewss.testPayment),
    re_path(r'^checkMiddleCode/pro/add$', viewss.testMiddleCodeCheck),
    re_path(r'^checkMiddleCode/', viewss.testCheckMiddleCode),
    re_path(r'^credit/pro/add$', viewss.testCreditReport),
    re_path(r'^credit/', viewss.testCredit),
    re_path(r'^token/pro/add$', viewss.testGetToken),
    re_path(r'^token/', viewss.testToken),

    re_path(r'^id/pro/add$', viewss.testGetId),
    re_path(r'^id/', viewss.testId),

    re_path(r'^user/pro/add2$', viewss.testRestPass),
    re_path(r'^user/pro/add$', viewss.testGetUser),
    re_path(r'^user/', viewss.testUser),

    # re_path(r'^pro/add', views.add_pr),
    # re_path(r'^pro/submit', views.proSubmit),
    # re_path(r'^testdb$', testdb.testdb),
]
