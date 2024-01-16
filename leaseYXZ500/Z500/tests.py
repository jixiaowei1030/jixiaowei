from django.test import TestCase

# Create your tests here.

code = 'AM40K8Y7C5P96S73'

print(code[14:16])
def checkzhongzhengma(code):
    if len(code) != 16:
        return False
    wi = [1,3,5,7,11,2,13,1,1,17,19,97,23,29]
    ci_position = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum = 0
    for i in range(14):
        tmp = ci_position.index(code[i])
        if tmp == -1:
            return False
        sum += tmp*wi[i]
    cb2 = sum%97 +1
    try :
        sl2 = int(code[14:16])
    except:
        return False
    rst = cb2==sl2
    return rst

if __name__ == "__main__":
    print(checkzhongzhengma(code))