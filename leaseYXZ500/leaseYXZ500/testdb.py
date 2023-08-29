from django.http import HttpResponse

from Z500.models import Test

# 数据库操作
def testdb(request):
    test1 = Test(name='yoyo1')
    test1.save()
    return HttpResponse("数据库hello_test添加name成功！看去看看吧")