def func1(arg1, arg2):
    var6 = func2(arg1, arg2)
    var19 = func4(arg1, var6)
    var24 = func5(arg1, arg2)
    def func6(arg25, arg26):
        var27 = arg25 & var6 | var19 + arg26
        var28 = var27 & -251846444 | arg2 | -1303730640 ^ -991 + var6 + var24 & (703365893 & arg25) & arg26 & (arg1 + (var24 ^ (var24 ^ arg1)) - ((var24 + ((39 & arg25 ^ -338 - arg26) + var6)) ^ var27) ^ var6)
        var29 = var28 - arg25 + ((((arg25 - var19) ^ -876) + (-976341933 & -1840029410 + ((-121 + var27) + arg26))) ^ (arg26 | var19)) & var27 & arg25 ^ var19 + var28
        result = arg1 & (arg1 ^ var19)
        return result
    var30 = func6(var6, var24)
    var35 = func7(arg2, var30)
    var36 = var6 | (var30 & var19) + arg1
    if var35 < var35:
        var37 = -104 | (-688 & var6)
    else:
        var37 = var24 - -751 & arg1 | arg1
    var38 = (var6 + arg1) & var35 - arg1
    if var6 < arg2:
        var39 = var24 & var35
    else:
        var39 = var19 | arg1
    if var36 < arg1:
        var40 = (arg1 + (826996759 - arg2)) ^ var35
    else:
        var40 = var38 | (var24 - arg2 & arg2)
    if var38 < var38:
        var41 = var19 ^ arg1 ^ 836 & var35
    else:
        var41 = var36 + (arg1 - -1647138100) ^ var36
    var42 = var36 & ((var6 ^ var35) & var6)
    var43 = (arg2 | 905 - var36) ^ var6
    var44 = var24 - (arg2 + var38)
    var45 = var30 | 939
    var46 = var43 ^ arg1
    var47 = (var19 & (var35 & var6)) ^ var6
    result = ((var35 - var6 ^ 844) - var19) | var35 - var38 - (var45 + (var24 & (var36 - (var24 | -918) + var46)))
    return result
def func7(arg31, arg32):
    var33 = 0
    for var34 in xrange(23):
        var33 += (arg32 | var33) + var33
    return var33
def func5(arg20, arg21):
    var22 = 0
    for var23 in range(42):
        var22 += 1 - arg20 - arg21
    return var22
def func4(arg7, arg8):
    var9 = arg8 - arg7 ^ arg8
    var10 = (var9 & var9 | -121) & arg8
    var11 = var9 - 920 ^ arg8
    var12 = (var11 + 486) | var9
    if var10 < var11:
        var13 = (var9 + var10) - var11 | arg7
    else:
        var13 = arg7 & var12
    var14 = var9 - arg7
    if var12 < var11:
        var15 = ((arg8 + var12) + arg7) | arg7
    else:
        var15 = (arg8 + var12 | var10) - arg7
    var16 = var9 ^ var9
    var17 = ((var11 | -741) - var12) | var10
    var18 = (var11 & arg8) - var16
    result = (var18 ^ arg7) - var18
    return result
def func2(arg3, arg4):
    def func3(acc, rest):
        var5 = (acc - acc) + -10
        if acc == 0:
            return var5
        else:
            result = func3(acc - 1, var5)
            return result
    result = func3(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 8'
    print 'arg_number: 48'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,