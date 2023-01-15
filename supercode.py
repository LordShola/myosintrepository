def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    var18 = var10(arg2, var7)
    var45 = var21(arg1, arg2)
    var50 = func9(var45, arg2)
    var55 = func10(var50, var45)
    var56 = ((822 & -447673105) | var45) | var18
    var57 = (var50 ^ var55 + arg2) ^ var45
    var58 = (arg1 + var18) ^ var7 | arg1
    var59 = var7 ^ arg2 - var56 - var7
    if var59 < var58:
        var60 = var50 - var7
    else:
        var60 = var58 - arg1
    var61 = var58 | -1548901617
    var62 = var59 - arg2 ^ var56 | var55
    var63 = arg1 - ((var56 | var61) & var7)
    var64 = ((var58 - arg1) - -1995905279) - var18
    var65 = (var62 ^ arg2) + arg2 ^ var45
    var66 = var59 - var61
    result = (var66 ^ var62) + (arg1 + (var55 + var45 ^ var55) | ((-51 - var64 - (var57 ^ var56)) - var66) ^ 2118641816)
    return result
def func9(arg24, arg25):
    var26 = -617 ^ 626276895
    var27 = (var26 ^ arg25 + arg25) - 816936491
    var28 = 985 ^ var27
    var29 = arg25 ^ arg24 - var26 & var27
    var30 = var29 | var27
    var31 = var27 + 108 & 763
    if var28 < arg24:
        var32 = arg24 | arg24 & var27 - arg24
    else:
        var32 = -580 ^ var26
    var33 = (var30 ^ var30) & var30
    var34 = -173381177 & var33
    var35 = arg25 & arg24
    var36 = (var30 ^ var28 - arg25) | -496
    var37 = ((-679 | var34) & var35) & arg25
    var38 = (var35 - var34 - -803) - var28
    var39 = (arg24 & arg24 + var31) ^ var28
    var40 = var33 + (arg24 & arg25) ^ arg24
    var41 = var28 | var40
    var42 = arg24 - arg25 | arg24
    var43 = 623 ^ var27 - 467
    result = 798665792 & var34 + var28
    return result

def func10(arg51, arg52):
    var53 = 0
    for var54 in xrange(10):
        var53 += (arg52 | -9) - arg51
    return var53
def func9(arg46, arg47):
    var48 = 0
    for var49 in xrange(29):
        var48 += arg46 & arg47 ^ var48
    return var48
def func8(arg22, arg23):
    var24 = 1226615762 & (arg22 | arg23) - arg22
    var25 = (930733718 - -361 + 2083817483) - var24
    var26 = 753 | arg22 | var25 + var25
    var27 = var26 | var26
    var28 = (var26 ^ -194152562) & (arg22 + var27)
    var29 = var26 - 218
    var30 = var24 + ((var27 + var28) - var29)
    var31 = var27 & var27
    var32 = var26 + var25
    var33 = var32 + (arg22 ^ arg23 | arg23)
    if var29 < var33:
        var34 = (var24 & var29) + var25 - var31
    else:
        var34 = (var27 - var33) ^ (var32 & var30)
    var35 = var25 + (var33 | arg23 ^ var26)
    var36 = (var26 + var28) | 977 - var26
    var37 = var36 ^ ((var35 & var31) + var32)
    var38 = (var35 | var35 + arg23) | var35
    var39 = var33 + (arg22 ^ var29) ^ var33
    var40 = var29 + arg22 & 1213098259 | var27
    var41 = var24 - (var32 | var35 + var32)
    if var35 < var28:
        var42 = var28 & var40
    else:
        var42 = var29 & var29
    if var37 < var33:
        var43 = (var30 - var32 ^ -274893867) + var37
    else:
        var43 = var30 ^ (arg22 & var32 & var24)
    var44 = var39 + arg22
    result = var31 & var41
    return result
def func7():
    closure = [-1]
    def func6(arg19, arg20):
        closure[0] += func8(arg19, arg20)
        return closure[0]
    func = func6
    return func
var21 = func7()
def func5(arg11, arg12):
    var13 = arg12 - (1254698193 - arg11 + -373085216 & arg12 + (-481497229 - arg12) | (arg11 | arg11) + arg12)
    var14 = arg11 - var13 & arg12 + arg11 | (((arg11 ^ var13) & (arg11 | var13 - arg12)) + 512) & (426 + arg11 | (((-73 - arg12) | arg11 & arg12 & var13 - -379) ^ arg12 & (-117 ^ 1934529830)))
    var15 = (arg12 - -1581335509 & var13) ^ var13 & (152 ^ var13 + arg12 & (var13 + var13 | ((var13 | arg11 & (var14 + 247) & var14) | arg12 & 1764779210 & var14) ^ var14 | var13 ^ var14 + var13)) - arg12
    var16 = var14 | arg11
    var17 = var16 - var16 + (arg11 - -674)
    result = -908 ^ var13
    return result
def func4():
    closure = [2]
    def func3(arg8, arg9):
        closure[0] += func5(arg8, arg9)
        return closure[0]
    func = func3
    return func
var10 = func4()
def func2(arg3, arg4):
    var5 = 0
    for var6 in range(28):
        if var5 < arg4:
            var5 += (var5 - arg4) + var6
        else:
            var5 += (var5 | var6) & 5
    return var5
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 67'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,