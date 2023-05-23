from django.http import JsonResponse
from .models import LibraryUser, KnowledgeUser


# Create your views here.
def register(request, keyword):
    if request.method == 'GET':
        username = request.GET.get('username') # 用户名
        password = request.GET.get('password')  # 密码
        repassword = request.GET.get('repassword') # 再次输入的密码
        name = request.GET.get('name')  # 姓名
        age = request.GET.get('age')   # 年龄
        gender = request.GET.get('gender') # 性别，值为1或2
        phone = request.GET.get('phone') # 电话号码
        email = request.GET.get('email') # 邮箱
        # 判断请求来自博物馆系统还是知识服务系统,设置flag的值
        if keyword == "keyword=LibraryUser":
            flag = 0
        elif keyword == "keyword=KnowledgeUser":
            flag = 1
        else:
            msg = 'url错误'
            data={
                'code': 404,
                'error_msg': msg
            }
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
            # 下面这句做测试用
            # return render(request, 'register.html')

        try:
            if flag == 0:
                user = LibraryUser.objects.get(UserName=username)
            else:
                user = KnowledgeUser.objects.get(UserName=username)

            if user:
                msg = "用户名已存在"
                data = {
                    'code':404,
                    'error_msg':msg,
                }
                return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
        except:
            if password != repassword:
                msg = "密码不一致"
                data = {
                    'code': 404,
                    'error_msg': msg,
                }
                return JsonResponse(data, json_dumps_params={'ensure_ascii':False})
            else:
                # 根据前面flag的值判断增加哪个数据库的记录
                if flag == 0:
                    newUser = LibraryUser()
                else:
                    newUser = KnowledgeUser()
                newUser.UserName = username
                newUser.PassWord = password
                newUser.Name = name
                newUser.Gender = gender
                newUser.Phone = phone
                newUser.Email = email
                newUser.Age = age
                newUser.Comment = True
                try:
                   newUser.save()
                   data={
                        'code': 200
                   }
                   return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
                except:
                    msg='数据类型不正确导致注册失败'
                    data={
                        'code': 404,
                        'error_msg': msg
                    }
                    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
    else:
        data={
            'code': 404,
            'error_msg': '请使用GET请求'
        }
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


def login(request, keyword):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        # print(username)
        # print(password)
        try:
            # 判断请求来自博物馆系统还是知识服务系统
            if (keyword == "keyword=LibraryUser"):
                user = LibraryUser.objects.get(UserName=username)
            elif (keyword == "keyword=KnowledgeUser"):
                user = KnowledgeUser.objects.get(UserName=username)
            else:
                msg = 'url错误'
                data = {
                    'code': 404,
                    'error_msg': msg
                }
                return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
                # 下面这句测试用
                # return render(request, 'login.html')

            if password == user.PassWord:
                if (user.Gender == 1):
                    gender = "男"
                else:
                    gender = "女"

                data = {
                    'code': 200,  # 登录成功
                    'username': user.UserName,
                    'password': user.PassWord,
                    'name': user.Name,
                    'age': user.Age,
                    'gender': gender,
                    'phone': user.Phone,
                    'comment': user.Comment,
                    'email': user.Email,
                }
                return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
            else:
                msg = "密码错误"
                data = {
                    'code': 404,
                    'error_msg': msg
                }
                return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
        except:
            msg = "用户名不存在"
            data = {
                'code': 404,
                'error_msg': msg
            }
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = {
            'code': 404,
            'error_msg': '请使用GET请求'
        }
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
