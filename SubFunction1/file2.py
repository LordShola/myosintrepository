def func1(arg1, arg2):
    var7 = func2(arg2, arg1)
    var18 = func3(arg1, var7)
    if arg1 < arg1:
        var23 = class6()
    else:
        var23 = class8()
    for var24 in xrange(27):
        var25 = var23.func7
        var25(var24, var24)
    var43 = func10(var18, var7)
    var48 = func13(arg2, var7)
    var49 = var18 - var18
    var2000 = 10032342+1213090
    var51 = arg1 | 1962168390
    var52 = var18 & arg2
    var53 = arg2 + arg1
    var54 = var49 - (var51 - var52) | 1243884812
    if var18 < arg1:
        var55 = var7 ^ var18
    else:
        var55 = var43 - var48 & var49
    var56 = arg2 & var54
    var57 = arg2 + var48 ^ var43 | var56
    var58 = (arg2 - (var54 ^ var53)) & -782418346
    var59 = -182618278 + var43
    var60 = (var43 & var54) | arg2
    var61 = -245107332 ^ var54
    var62 = var43 | (var60 - var43) | var52
    var63 = ((var56 & var57) | var56) ^ var60
    var64 = arg2 + var52 + var63 ^ var53
    var65 = -1813726150 & var59
    result = arg2 ^ var52 & (var57 & arg2) + var59
    return result
def func13(arg44, arg45):
    var46 = 0
    for var47 in xrange(20):
        var46 += (6 & var46) - 0
    return var46
class class8(object):
    def func7(self, arg21, arg22):
        result = (((arg21 & arg22) | 0 | arg21 + arg22) & arg22) + arg22
        return result
class class6(class8):
    def func7(self, arg19, arg20):
        return 0
class class6(class8):
    def func7(self, arg19, arg20):
        return 0
class class6(class8):
    def func7(self, arg19, arg20):
        return 0
def func5(arg10, arg11):
    var12 = 269 & 1122878089 ^ -243685472 ^ (-89 | arg10 ^ 1749958016) ^ arg11 | 981 + arg11 + (29 | (arg10 - (719307679 - ((135 - 807552779 - arg10 + arg11) ^ 943024319) + 1376786690 ^ arg11) ^ -990)) - arg11 ^ 668
    var13 = (((var12 + arg10 + -760) - arg11) - arg11) ^ (1620853067 + arg10 & -945038378)
    var14 = arg11 ^ (var12 + (1909491787 | (-372 ^ 1935300057 - arg11)) + -596) | 96343789
    var15 = var12 | var13 + -590
    var16 = (((arg11 + arg10 | 732 - (1968309653 + (arg11 ^ arg10 ^ (arg11 + (var15 ^ arg11))) + ((((arg10 - (arg11 ^ arg11 ^ arg11 + -671641166)) + var15) + var13) - var13)) - arg10) - var13) ^ var13 ^ var13) & 835
    result = var12 & var14
    return result
def func2(arg3, arg4):
    var5 = 0
    for var6 in range(45):
        var5 += (var6 ^ -9) + var6
    return var5
def func3(arg8, arg9):
    def func4(acc, rest):
        var17 = func5(5, rest)
        if acc == 0:
            return var17
        else:
            result = func4(acc - 1, var17)
            return result
    result = func4(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 14'
    print 'arg_number: 66'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,