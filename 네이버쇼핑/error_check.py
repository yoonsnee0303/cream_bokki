# def error_ck_test(para):
#     print(para)
#     if para == 'arg':
#         return 'error'

# while True:
#     test = error_ck_test('arg')
#     if test == 'error':
#         pass
#     else:
#         break

camaler_case = 'myFun'
snake_case = "my_fun"
capital_case = 'MyFun'


def myFun(파라미터):
    while True:
        try:
            x = 파라미터
            return x
        except:
            return 'error'


myFun('아규먼트')