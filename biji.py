#coding:utf-8
##demo 编码

##数据输出到文件中,
##注意点，1、所指定的盘符必须存在，2、使用file=fp
#fp=open('D:/text.txt','a+')
#print(520,file=fp)

##不进行换行输出（输出内容在一行当中,使用逗号进行分割，就会在一行内进行输出）
#print('hello','world','Python',file=fp)
#fp.close()

##转义字符
#print('1、hello\nworld') #\ +转义功能的首字母__n-->newline的首字符表示换行
#print('2、hello\tworld') #hello    world
#print('3、hello\rworld') #world
#print('4、hello\bworld') #hellworld
#print('5、http:\\\\www.baidu.com') #http:\\www.baidu.com
#print('6、老师说：\'大家好\'') #老师说：'大家好'

##原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或R
#print(r'7、hello\tworld') #hello\tworld
##注意事项：最后一个字符不能是反斜杠，但可以是两个反斜杠  print(r'hello\tworld\')
#print(r'hello\tworld\\') #hello\tworld\\

##字符转换
#print(chr(0b100111001011000)) #乘 二进制100111001011000=十进制20056=十六进制4e58
#print(ord('乘')) # 十进制20056=二进制100111001011000 无论多少进制最后都会转变为二进制，因为计算机只认识二进制

##保留字符
#import keyword
#print(keyword.kwlist) # 输出的字符都是保留字符，不能进行命名

##标识符规则，字母、数字、下划线_。但是不能以数字开头，不能是保留字符，严格区分大小写。
##变量的定义和使用，变量是内存中一个带标签的盒子
##变量由三部分组成
## 1、标识：表示对象所存储的内存地址，使用内置函数id（obj）来获取
## 2、类型：表示的是对象的数据类型，使用内置函数type（obj）来获取
## 3、植：表示对象所存储的具体数据，使用print(obj)可以将植进行打印输出
#name = '李晓辉' #定义一个变量，并且赋予变量的值为李晓辉，并且它存贮着id、type、value。
#print(name) # 李晓辉
#print('标识',id(name)) # id=1916438344880
#print('类型',type(name)) # type=str
#print('值',name) # value:'李晓辉'

##多次赋值之后，变量名会指向新的空间
#name='李晓辉' # 这个就会变为内存垃圾，会有垃圾回收机制进行回收
#name='carry' # 这时就会指向新的空间
#print(name) # carry

## 这样可以更好的理解，我们在赋值一次后进行输出，会发现，第一行的输出是carry，而第二行的输出就是李晓辉，这就是指向最新的空间
#name='carry'  
#print(name) 
#name='李晓辉'
#print(name) 

##数据类型，常用的数据类型：

##整数可以表示为二进制、十进制、八进制、十六进制，默认十进制,十进制是默认的进制，二进制以0b开头，八进制以0o开头，十六进制以0x开头
##整数类型：int 100 英文integer，可以表示正负数和零
#n1=90
#n2=-90
#n3=0
#print(n1,type(n1)) # 90 <class 'int'>
#print(n2,type(n2)) # -90 <class 'int'>
#print(n3,type(n3)) # 0 <class 'int'>
#print('十进制',8888) # 十进制 8888
## 十进制，基本数：0，1，2，3，4，5，6，7，8，9 遇10进1
#print('二进制',0b0010001010111000) # 二进制 8888
## 二进制，基本数：0，1 遇2进1
#print('八进制',0o21270) # 八进制 8888
## 八进制，基本数：0，1，2，3，4，5，6，7 遇8进1
#print('十六进制',0x22b8) # 十六进制 8888
## 十六进制，基本数：0，1，2，3，4，5，6，7，8，9，A,B,C,D,E,F 遇16进1

##浮点数类型：float 3.14159
##使用浮点数类型进行计算，有些会不精确，比如下面的案例
#a=1.1
#b=2.2
#print(a,type(a)) # 1.1 <class 'float'>
#print(a+b) # 3.3000000000000003
##如何精确？可以导入模块进行修正
#from decimal import Decimal
#print(Decimal('1.1')+Decimal('2.2')) # 此时的输出就是会变成3.3

##布尔类型：bool True，False ##他比较特殊，只有两个值，是或否，注意python中的bool是可以转成整数进行计算
#a=True
#b=False
#print(a,type(a)) # True <class 'bool'>
#print(a+1) # 2，因为1+1=2

##字符串类型：str '全体起立'，又称为不可变的字符序列，可以使用单引号、双引号、三引号，注意三引号可以分布在连续的多行，而单引号和双引号只能在一行
#str1 = '全体起立' # 全体起立 <class 'str'>
#str2 = "全体起立" # 全体起立 <class 'str'>
#str3 = """全体起立 
#LBWNB""" 
##全体起立
##LBWNB <class 'str'>
#str4 = '''全体起立
#LBWNB'''
##全体起立
##LBWNB <class 'str'>
#print(str1,type(str1))
#print(str2,type(str2))
#print(str3,type(str3))
#print(str4,type(str4))

##demo
#name='李晓辉'
#age=22
#print(name,type(name),age,type(age))
##print('我叫'+name+'今年'+age+'岁') # 如果这样进行输出，他会报错，因为它的类型不一致，需要转换，加号是连接符
#print('我叫'+name+',今年'+str(age)+'岁') # 我叫李晓辉,今年22岁 这里我们将int转换为了字符串，类型一致了就不会报错

##demo str()将其它类型转为str类型
#a=10
#b=10.01
#c=False
#print (a,type(a),b,type(b),c,type(c)) # 10 <class 'int'> 10.01 <class 'float'> False <class 'bool'>
#print (str(a),str(b),str(c)) # 10 10.01 False

##demo int()将其它类型转为int类型，注意：文字和小数类字符串，无法转整数，浮点数转整数，抹零取整
#a='128'
#b=128.7
#c='128.7' #会报错
#d=True
#e='hello' #会报错
#print (int(a)) # 128
#print (int(b)) # 128
#print (int(c)) # ValueError: invalid literal for int() with base 10: '128.7' 会报错
#print (int(d)) # 1
#print (int(e)) # ValueError: invalid literal for int() with base 10: 'hello' 会报错


##demo float()将其它类型转为float类型，注意：文字无法转为整数，整数转浮点数，末尾为.0
#a='128.7'
#b='128' 
#c=True
#d=128
#e='hello'
#print(type(a),type(b),type(c),type(d),type(e)) # <class 'str'> <class 'str'> <class 'bool'> <class 'int'> <class 'str'>
#print(float(a)) # 128.7
#print(float(b)) # 128.0
#print(float(c)) # 1.0
#print(float(d)) # 128.0
#print(float(e)) # could not convert string to float: 'hello' 会报错,字符串中的数据如果是非数字穿，则不允许转换

##demo 注释
#print('hello') #单行注释
''' 
李晓辉牛逼，三引号为多行注释
牛逼
'''

##demo 输入函数 input
#a=input('李晓辉想要什么礼物呢？') # 女朋友
#print(a,type(a)) # 女朋友

##case1 从键盘录入两个整数，计算两个整数的和
# a=input('请输入一个正整数') # 1
# b=input('请输入一个正整数') # 2
# print(type(a),type(b)) # <class 'str'> <class 'str'>
# print(int(a)+int(b)) # 3 

# a=int(input('请输入一个正整数')) # 1
# b=int(input('请输入一个正整数')) # 2
# print(type(a),type(b)) # <class 'int'> <class 'int'>
# print(a+b) # 3

# a=input('请输入一个正整数') 
# b=input('请输入一个正整数')
# c=int(a)
# d=int(b)
# print(type(a),type(b),type(c),type(d)) # <class 'str'> <class 'str'> <class 'int'> <class 'int'>
# print(c+d)


##demo 常用运算符——算术运算符——标准运算符——加(+)、减(-)、乘(*)、除(/)、整除(//)
# print(1+1) # 加法运算
# print(1-1) # 减法运算
# print(2*4) # 乘法运算
# print(4/2) # 除法运算
# print(11//2) # 整除运算

##demo 常用运算符——算术运算符——取余运算符(%)
# print(11%2) # 取余运算，因为11/2=5，余1 

##demo 常用运算符——算术运算符——幂运算符(**)
# print(2**2) # 表示2的2次方 4
# print(2**3) # 表示2的3次方 8

##正负整除
# print(9//4)     # 2 ++=+ 整除 正正得正
# print(-9//-4)   # 2 --=+ 整除 负负得正
# print(9//-4)    # -3 +-=- 一正一负整数运算，向下取整，就是取比自己小的最大整数，例：-2.2 取 -3

## 正负取余
# print(9%-4)     # 公式 余数=被除数-除数*商 9-(-4)*(-3) --> 9-12 --> -3
# print(-9%4)     # 公式 余数=被除数-除数*商 -9-(4)*(-3) --> -9+12 --> 3

##demo 常用运算符——赋值运算符 执行顺序从右到左
# a=6+9
# print(a)

## 支持链式赋值
# i=1+2
# print(i)
# a=b=c=20
# print(a,id(a))    # 20 140708066853744
# print(a,id(b))    # 20 140708066853744
# print(a,id(c))    # 20 140708066853744
#内存中有这么一个对象，value：20，id：140708066853744，type：int。然后a指向了它，b也指向了它，c也指向了它

## 支持参数赋值
# a=20
# a+=30   # 50 相当于a=a+30
# print(a,type(a)) # 50 <class 'int'>
# a-=10   # 40 相当于a=a-10
# print(a,type(a)) # 40 <class 'int'>
# a*=2    # 80 相当于a=a*2
# print(a,type(a)) # 80 <class 'int'>
# a/=3    # 26.666666666666668 相当于a=a/3
# print(a,type(a)) # 26.666666666666668 <class 'float'>
# a//=2   # 13.0 相当于a=a//2
# print(a,type(a)) # 13.0 <class 'float'>
# a%=3    # 1.0 相当于a=a%3
# print(a,type(a)) # 1.0 <class 'float'>

## 支持系列解包赋值,左右两边的变量数和值要相同，有多少个值就要多少个变量，一对一。
# a,b,c=1,2,3 # a=1,b=2,c=3
# print(a,b,c) # 1 2 3

## 交换两个变量的值
# a,b=10,20
# print('交换之前',a,b)   # 交换之前 10 20
# a,b=b,a # 交换
# print('交换之后',a,b)   # 交换之后 20 10

## input函数知识点:1、用于接收用户输入 2、返回值为str 3、使用=赋值变量存储
# 以下案例需要各位思考，当我们变量b输入的不是int的时候该怎么办？异常如何处理
# a=1
# b=input('请输入数字')
# if (type(b) != int):
#     b=int(b)
#     b=input('您的输入有误，请输入数字')
# else:
#     print(type(b))
# print(int(b)-a)

# ctrl+/ 快速注释

## 比较运算符 >,<,>=,<=,==,!=,is,is not
# a,b=10,20
# print('a>b?',a>b) #False
# print('a<b',a<b) #True
# print('a<=b?',a<=b) #True
# print('a>=b?',a>=b) #False
# print('a==b?',a==b) #False
# print('a!=b?',a!=b) #True

'''
一个 = 称为赋值运算符，==称为比较运算符
一个变量由三部分组成，标识，类型，值
==比较的是值还是表示？比较的是值
比较对象的标识使用 is
因为a=10这个变量，里面包含了ID和类型，值
看下面的例子
'''
# a=10
# b=10
# print(a==b) #True 说明，a与b的value 相等
# print(a is b) #True 说明，a与b的id标识，相等

# lst1=[11,22,33,44]
# lst2=[11,22,33,44]
# print(lst1==lst2) #True
# print(lst1 is lst2) #False 虽然内容都一样，但是他们的ID是不同的
# print(id(lst1)) #2403143134208
# print(id(lst2)) #2403147649152
# print(lst1 is not lst2) # is not:是不相等的嘛？

## 布尔运算符 and是与，or是或，not是非
# a,b=1,2
# and
# print(a==1 and b==2) # True,and的意思两边都需要符合才是True
# print(a==1 and b<2) # False,因b=2,不小于2
# print(a!=1 and b==2) # False,因a==1
# or
# print(a==1 or b==2) # True,or的意思两边当中满足一个即可
# print(a==1 or b<2) # True,因a==1
# print(a!=1 or b==2) # True，因b==2
# print(a!=1 or b!=2) # False,因两边都不满足
# not 取反，对就是错，错就是对，对bool类型操作数取反
# f1=True
# f2=False
# print(not f1) # False
# print(not f2) # True
# in 判断是否包含
# lst1=[1,2,3,4,5]
# print(1 in lst1) # True
# print(10 in lst1) # False
# print(1 not in lst1) # False
# print(10 not in lst1) # True
# lmy='helloworld'
# print('s' in lmy) # False
# print('o' in lmy) # True

## 位运算符 将数据转为二进制进行计算
'''
&:对应数位都是1，才为1
|：对应数位都是0，才为0
<<:左移位运算符，向左移动位置，高位溢出，低位补0,向左移动n位，没有1溢出的时候结果就是乘以2^n
>>:右移位运算符，向右移动未知，低位溢出，高位补0,向右移动n位，没有1溢出的时候结果就是除以2^n
'''
# print(4&8) # 00000100 & 00001000 = 00000000 = 0
# print(4&6) # 00000100 & 00000110 = 00000100 = 4
# print(4|8) # 00000100 | 00001000 = 00001100 = 12
# print(4<<1) # 00000100 << 1 = 00001000 = 8
# print(4<<2) # 00000100 << 2 = 00010000 = 16
# print(4>>1) # 00000100 >> 1 = 00000010 = 2
# print(4>>2) # 00000100 >> 2 = 00000001 = 1

# Python中的运算符,通常情况下，第一优先级算术运算符(**、*，/，//，%、+，-),第二优先级位运算(<<,>>、&、|),
# 第三优先级比较运算符(>,<,>=,<=,==,!=),第四优先级布尔运算符(and、or),第五优先级赋值运算符(=),如果有括号则先算括号内

## 程序的组织结构
'''
1996年，计算机科学家证实任何简单或复杂的算法都可以由顺序结构、选择结构和循环结构这三种基本结构组合而成
计算机的控制流程
1、顺序结构
2、选择结构 if语句
3、循环结构 for-in语句，while语句
'''
## 顺序结构——把大象装冰箱分几步？
# print('1,把冰箱门打开')
# print('2,把大象放冰箱里')
# print('3,把冰箱门关上')

## Python一切皆对象，所有的对象都有一个布尔值，也就说真和假，如何获取bool()
# 以下对象的布尔值为False:False、数值0、None、空字符串、空列表、空元组、空字典、空集合
# print(bool(False)) # False
# print(bool(0)) # 数值0
# print(bool(None)) # None
# print(bool('')) # 空字符串
# print(bool("")) # 空字符串
# print(bool([])) # 空列表
# print(bool(list())) # 空列表
# print(bool(())) # 空元组
# print(bool({})) # 空字典
# print(bool(dict())) # 空字典
# print(bool(set())) # 空集合

## 选择结构
#单分支结构
# balance=1000 # 余额
# WM=int(input('请输入取款金额'))

# if balance >= WM:
#     balance=balance-WM
#     print('您已取款',WM,'元')
#     print("余额：",balance)

#双分支结构
# a=int(input('请从键盘录入一个整数'))

# if a%2 == 0:
#     print('您输入的数是一个偶数')
# else:
#     print('您输入的数是一个奇数')

#多分支结构
# achievement=int(input('请输入您的成绩'))

# if achievement == 100:
#     print('恭喜您，您可是真是个天才')
# elif 80<= achievement <=99:
#     print('可以可以，有点厉害')
# elif 60<= achievement <=79:
#     print('再接再厉')
# elif achievement <60 and achievement >= 0:
#     print('不会吧不会吧，不会真的有人不及格吧')
# else:
#     print('总分100，请输入0-100以内的数字')

#嵌套if
#判断是否会员，并对应价格进行折扣
# A=1234 #会员
# B=4321 #非会员
# Total_price=float(input('请输入总价'))
# C=int(input('请输入账号'))

# if C == A:
#     if 100<= Total_price <= 1000:
#         Total_price = Total_price*0.9
#         print (Total_price,'9折优惠')
#     elif 1001<= Total_price <= 5000:
#         Total_price = Total_price*0.75
#         print (Total_price,'7.5折优惠')
#     elif 5001<= Total_price <=10000:
#         Total_price = Total_price*0.65
#         print (Total_price,'6.5折优惠')
#     else:
#         print('不好意思，您输入的价格不在此次活动范围，请咨询前台工作人员获得帮助')
# else:
#     print('不好意思，您不是会员，不能参与折扣活动')

## 条件表达式
# num_a=int(input('第一个数'))
# num_b=int(input('第二个数'))

# print('使用条件表达式进行比较') #前半部分为True,中间为判断规则，后半部分为False
# print(str(num_a)+'大于'+str(num_b) if num_a>num_b else str(num_a)+'小于'+str(num_b) ) #此处牢记，如果需要数字加中文进行输出，先将数字变量转为字符串类型，然后再链接

## pass 语句，什么都不做,只是一个占位符,用于需要写语句的地方
# a=int(input('请从键盘录入一个整数'))

# if a%2 == 0:
#     pass #此处语法不报错
# else:
#     print('您输入的数是一个奇数')

## 转圈圈-第五章函数、range()函数的使用、while循环、for-in循环、break、continue与else语句、嵌套循环
#内置函数range() 不需要加任何前缀可以直接使用的函数，它的作用是生成一个整数序列，三种创建方式
#第一种创建方式，只有一个参数(小括号中只给了一个数) range(stop)
# r=range(10) # 默认从0开始，默认每个数之间相差1称为步长，[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(r) # range(0,10)
# print(list(r)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#第二种创建方式,两个参数 range(start,stop)
# r=range(1,10) # 这里我们指定了起始值为1，从1开始，到10结束(不包含10),默认步长还是1
# print(r) # range(1,10)
# print(list(r)) # [ 1, 2, 3, 4, 5, 6, 7, 8, 9]

#第三种创建方式，三个参数 range(start,stop,step)
# r=range(1,10,2) # 这里我们指定了起始值为1,从1开始,到10结束(不包含10),并且设置步长为2,也就是数与数之间隔两个数
# print(r) # range(1,10,2)
# print(list(r)) # [1, 3, 5, 7, 9]
# #如何判断指定的整数,在序列中是否存在，in、not in
# print(10 in r) # 返回布尔值 False
# print(5 in r) # True
# print(10 not in r) # True
# print(5 not in r) # False

#总结# range类型的优点:不管range对象表示的整数序列有多长,所有range对象占用的内存空间都是相同的,因为只需要存储start、stop、step，而且只有当用到range对象时才会去计算序列中的相关元素

## 循环结构
#当a小于10的时候,a+1返回,再次计算判断,直到a不小于10,跳出
# a=1
# while a<10:
#     print(a)
#     a+=1

'''
计算0到4之间的累加和,4步循环法:
1.初始化变量
2.条件判断
3.条件执行体(循环体)
4.改变变量
总结:初始化的变量与条件判断的变量与改变的变量为同一个
'''
# sum=0 # 用于存储累加和
# a=0 # 初始化变量为0
# while a < 5:
#     sum+=a # 条件执行体(循环体) True
#     a+=1
#     print(sum,a)
# print('和为',sum) # False

## 计算1-100之间的偶数和
# a=1
# sum=0
# while a < 101:
#第一种写法
    # a+=1
    # if a%2==0:
    #     sum+=a
#第二种写法
    # a+=1
    # if not bool(a%2):
    #     sum+=a
#第三种写法
    # a+=1
    # if a%2!=0:
    #     sum+=a  
    #     sum-=1
# print(sum)

## for-in循环
'''
·in:表达从(字符串、序列等)中依次取值，又称为遍历
 for-in遍历的对象必须是可迭代对象
·for-in的语法结构:for 自定义的变量 in 可迭代的对象:循环体
'''

# for item in 'Python': # 第一次取出来的是P，将P赋值item，将item输出，第二次取出来的是y，将y赋值item，将item输出，依此类推
#     print(item)

#range() 产生一个整数序列,也是一个可迭代对象
# for i in range(2,10,2):
#     print(i)

#如果在循环体中不需要使用到自定义变量,可将自定义变量写为“_”
# for _ in range(5):
#     print('人生苦短,我用Python')

#test:使用for循环,计算1到100之间的偶数和
# sum=0
#第一种写法
# for i in range(2,102,2):
#     if i != 100:
#         sum+=i
#     else:
#         print(sum)

#第二种写法
# for i in range(1,100):
#     if i%2==0:
#         sum+=i
# print(sum)

#第三种写法
# for i in range(1,100):
#     if i%2!=0:
#         sum+=i
#         sum-=1
# print(sum)

## test:输出100到999之间的水仙花数 ps:"所谓的“水仙花数”是指一个三位数其各位数字的立方和等于该数本身，例如153是“水仙花数”，因为：153 = 1³ + 5³ + 3³。"
# for item in range(100,1000):
#     g=item%10       #取个位的数
#     s=item//10%10   #取十位的数
#     b=item//100     #取百位的数
#     if g**3+s**3+b**3==item: # 如何幂运算 **
#         print(item)

#幂运算例子：
# for i in range(1,20):
#     i=i**2
#     print(i)

## break 循环结束语句,看下方两个程序的不同,没有break会一直继续执行下去,有break则结束
# password=int(1999)
# for pw in range(1800,2100):
#     if pw == password:
#         print(pw)
#     elif pw == 1806:
#         print('error')
#error
#1999

# password=int(1999)
# for pw in range(1800,2100):
#     if pw == password:
#         print(pw)
#     elif pw == 1806:
#         print('error')
#         break
# #error
        
##continue 用于结束当前循环，进入下一次循环，通常与分支结构中的if一起使用
#输出1到50之间的所有5的倍数,要求使用continue
# for i in range(1,51):
#     if i%5==0:
#         print(i)

#使用continue
# for i in range(1,51):
#     if i%5!=0:
#         continue
#     print(i)

''' 
else:与else语句搭配使用的三种情况
1、if else，if条件表达式不成立时执行else
2、while else，没有碰到break时执行else，简单点说就是没有break的话，就会循环完执行else
3、for else，没有碰到break时执行else，简单点说就是没有break的话，就会循环完执行else
'''
## for else
# for i in range(3):
#     pwd=int(input('please input your password'))
#     if pwd == 8888:
#         print('right')
#         break
#     else:
#         print('error')
# else:
#     print('your try too more error,please wait')


## while else
# a=0
# while a<3:
#     pwd=int(input('please input your password'))
#     if pwd == 8888:
#         print('right')
#         break
#     else:
#         print('error')
#         a+=1
# else:
#     print('your try too more error,please wait')

## 嵌套结构,套娃循环
#输出一个三行四列的矩形
#tips:end='\t'就是不换行的意思，下一行print()是换行的意思
# for i in range(1,4):
#     for a in range(1,5):
#         print('*',end='\t')
#     print()

#输出九九乘法表
# c=0
# for i in range(1,10):
#     for a in range(1,i+1): #为什么是i+1?因为range(1,2)等于输出 1 ，range(1,3)等于输出1,2,所以我们需要i+1,而不是加0，此处建议加上断点运行方便理解
#         c=a*i
#         print(a,'*',i,'=',c,end='\t')
#     print()

## tips:Python中一切皆对象

## 列表的查询操作
'''
index()
1. 如查询列表中存在N个相同元素，只返回相同元素中的第一个索引
2. 如查询的元素不存在，则会抛出ValueError
3. 还可以在指定的satrt和stop之间进行查找

获取单个元素
1. 正向索引从0到N-1 举例:lst[0]
2. 逆向索引从N-1到0 举例:lst[-N]
3. 指定索引不存在，抛出IndexError
'''
# lst1=['hello','world',66,'world'] # 正的:0→hello,1→world,2→66 反的:-1→66,-2→world,-3→hello, 每个元素都有索引,正的:0,1,2,3,4..... 反的:-1,-2,-3,-4.........
# lst2=list(['hello','lxh',25]) # 列表的两种写法

# print(lst1[1]) # world
# print(lst1.index('world')) # 1,即使有两个world他也只会输出第一个
# print(lst1.index('world',0,4,)) # 1,指定start和stop之间查找
# # print(lst2[6]) # IndexError:list index out of range,表示查询的索引不存在列表中
# # print(lst1.index('lxh')) #ValueError:'lxh' is not in list,表示查询的元素不在列表中

# lst3=[10,20,30,40,50,60,70,80]
# print(lst3[1:6:2]) # 第一个数字是开始,第二个数字是结束,记住左开右闭,第三个数字是步长
# lst2=(lst3[1:6:1])
# print(lst3,id(lst3)) # [10, 20, 30, 40, 50, 60, 70, 80] 1799909026816
# print(lst2,id(lst2)) # [20, 30, 40, 50, 60] 1799909347392
# 正数:
# 默认步长
# print(lst3[1:6:]) # [20, 30, 40, 50, 60]
# 默认起始
# print(lst3[:6:1]) # [10, 20, 30, 40, 50, 60]
# 默认结束
# print(lst3[1::1]) # [20, 30, 40, 50, 60, 70, 80]
# 负数:
# 步长为负数
# print(lst3[::-1]) # [80, 70, 60, 50, 40, 30, 20, 10]
# print(lst3[7::-1]) # [80, 70, 60, 50, 40, 30, 20, 10]

# 判断元素是否在列表当中
# lst4=[10,20,'python','hello']
# print(10 in lst4) # True
# print(10 not in lst4) # False
#列表元素的遍历
# for item in lst4:
#     print(item)

## 列表元素的增加操作
# 列表的末尾添加一个元素
# lst5=[1,2,3,4,5]
# lst6=[5,4,'hello','lxh']
# print(lst5,id(lst5)) # [1, 2, 3, 4, 5] 2578291174400
# lst5.append(10) # 尾部加一个10元素
# print(lst5,id(lst5)) # [1, 2, 3, 4, 5, 10] 2578291174400
# 列表的末尾添加多个元素 extend()
# lst5.append(lst6) # [1, 2, 3, 4, 5, [5, 4, 'hello', 'lxh']]
# lst5.extend(lst6) # [1, 2, 3, 4, 5, 5, 4, 'hello', 'lxh']
# 列表指定位置插入元素 insert()
# lst5.insert(2,2.5) # [1, 2, 2.5, 3, 4, 5]
# 切片,在列表的指定位置插入覆盖多个元素
# lst5[3:]=lst6 # [1, 2, 3, 5, 4, 'hello', 'lxh'],3指的就是从第三个数开始插入
# print(lst5)

## tips:快速创建列表
# lst7 = [i for i in range(10)] 
# print(lst7) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# lst7 = []
# for i in range(10):
#     lst7.append(i)
# print(lst7) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# lst7 = []
# for i in range(10):
#     lst7 += [i]
# print(lst7) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# i=-1
# lst7=[]
# while i < 9:
#  i+=1
#  lst7.append(i)
# print(lst7) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

## 列表元素的删除操作
# lst7 = [i for i in range(1,10,2)] 
# lst7.remove(5) # 移除为5的元素,如果有多个重复元素,只会移除第一个,如果元素不存在则会ValueError
# print(lst7) # [0, 1, 2, 3, 4, 6, 7, 8, 9]
# lst7.pop(5) # 移除索引为5的元素,如果移除的索引不存在,将抛出异常
# print(lst7) # [0, 1, 2, 3, 4, 6, 7, 8, 9]
# lst7.pop() # 如果不写东西,则默认移除最后一个数
# print(lst7) # [0, 1, 2, 3, 4, 5, 6, 7, 8]
# lst8=lst7[1:5] # 对列表进行切片,切片后会产生新的对象
# print(lst8) # [1, 2, 3, 4]
# lst7[1:5]=[] # 对列表进行切片删除,并用空列表替代,从而不会产生新的对象
# print(lst7) # [0, 5, 6, 7, 8, 9]
# lst7.clear() # 清楚列表中的所有元素
# print(lst7)
# del lst7 # 直接删除列表,使之报错
# print(lst7) # NameError: name 'lst7' is not defined

## 列表元素的修改操作
# lst8=[1,2,3,4,5,6,7,8,9,10]
#第一种修改方式,通过修改索引的方式
# lst8[2]=10
# print(lst8)
#第二种修改方式,批量修改
# lst8[1:4]=[10,20,30,40,50]
# print(lst8)

## 列表的排序方式
# lst9 = [1,9,7,5,4,8,3,2,6] 
#第一种:由大到小排序 sort()
# lst9.sort(reverse=True) #从大到小,降序排序，反过来reverse=False就是升序排序
# print(lst9)
#第二种:由大到小排序 sorted,此方法会产生新的列表对象
# lst10=sorted(lst9) # 默认从小到大
# lst10=sorted(lst9,reverse=True) #加上reverse=True就变成了降序排序
# print(lst9,id(lst9))
# print(lst10,id(lst10))

## 字典 特点:不可变序列,hash(key)不变
#字典创建方式一:
# scores={'l':133,'x':114,'h':8030} # {'l': 133, 'x': 114, 'h': 8030}
#字典创建方式二：
# scores=dict(name='jack',age=10) # {'name': 'jack', 'age': 10}
# print(scores)
#字典创建方式三：828-838行
#空字典:
# d={}
# print(d)

## 获取字典中的value
# scores={'l':133,'x':114,'h':8030} # {'l': 133, 'x': 114, 'h': 8030}
#第一种方式:
# print(scores['h'])
# print(scores['q']) #如果查找的键不存在,报KeyError错误

#第二种方式：
# print(scores.get('h'))
# print(scores.get('q')) #如果查找的键不存在,默认返回None
# print(scores.get('q',99)) #并且get可以设置查找不到key的返回值，比如:这里我们设置,查找不到q,则返回99

#这两种方式的不同之处在于,如果查找的键不存在,[]的方式会报错,但是get方式不会报错

# key的判断
# scores={'l':133,'x':114,'h':8030} # {'l': 133, 'x': 114, 'h': 8030}
# print('q'in scores) # q在scores字典中? False
# print('q' not in scores) # q不在scores字典中? True

# key的删除
# del scores['l']
# print(scores) #  {'x': 114, 'h': 8030}

# 清空字典
# scores.clear()
# print(scores)

# key的增加
# scores['y']=189
# print(scores)

# key的修改
# scores['l']=189
# print(scores)

# 键盘输入一个数并储存到字典里面
# scores['y']=(input('请输入'))
# print(scores)

# 循环输入十个数到字典里面
# scores={}
# for i in range(1,11):
#     scores[i]=input('请输入')
#     print(i)
# print(scores)

## 获取字典视图,Keys() 获取字典中所有key,values() 获取字典中所有value,items() 获取字典中所有key,value对。
# scores={'l':133,'x':114,'h':8030} # {'l': 133, 'x': 114, 'h': 8030}

# 获取所有的key
# keys=scores.keys()
# print(keys)
# print(type(keys))
# print(list(keys)) # 将所有的可以组成的视图转成列表

# 获取所有的value
# values=scores.values()
# print(values)
# print(type(values))
# print(list(values))

# 获取所有的key-value对
# items=scores.items()
# print(items)
# print(list(items)) # ()元组

# 字典匀速的遍历
# for item in scores:
#     print(item,scores[item],scores.get(item))

'''
字典的特点 总结:
· 字典中的所有元素都是一个key-value对，key不允许重复，value可以重复
· 字典中的元素是无序的，如果需要插入元素，不能指定位置插入，列表可以
· 字典中的key必须是不可变对象，列表是可变对象
· 字典也可以根据需要动态地伸缩
· 字典会浪费较大的内存，是一种使用内存换时间的数据结构，但是字典查找快
'''
## 字典生成式
# items=['Fruits','Books','Others']
# prices=[96,78,85]

# lxh=zip(items,prices) # 列表
# print(list(lxh))

# lxh={item:price   for item,price in zip(items,prices)} # {'Fruits': 96, 'Books': 78, 'Others': 85}
# lxh={item:prices  for item,price in zip(items,prices)} # {'Fruits': [96, 78, 85], 'Books': [96, 78, 85], 'Others': [96, 78, 85]}
# lxh={item.upper():price  for item,price in zip(items,prices)} # {'FRUITS': 96, 'BOOKS': 78, 'OTHERS': 85}
# print(lxh)

## 元组
'''
元组：Python内置的数据结构之一，是一个不可变序列

不可变序列与可变序列
· 不可变序列：字符串、元组
    · 没有增、删、改的操作
· 可变序列：列表、字典
    · 可以对序列执行增、删、改操作，对象地址不发生更改
'''

## 元组创建方式
# 一、小括号
# l=('l','x','h',2012)

# 二、不加括号
# l='l','x','h'

# 三、内置函数tuple()
# l=tuple(('l','x','h',2012))

# 如果元组中只有一个元素，那么逗号不能省
# l=('lxh',)
# print(l)
# print(type(l))

# 空元组创建方式
# a=tuple()
# a=()
# print(a)
# print(type(a))

'''
提问为什么需要将元组设计成不可变序列?
因为在多任务环境下，同时操作对象时不需要加锁，因此，在程序中尽量使用不可变序列

注意事项：元组中存储的是对象的引用
    (a)如果元组中的对象本身不可变对象，则不能再引用其它对象
    (b)相反，如果元组中的对象是可变对象，则可变对象的引用不允许改变，但是数据可以更改
'''
# 例子：
# a=(10,[20,30],40) # (10, [20, 30], 40)
# a[1].append(35) # (10, [20, 30, 35], 40)
# print(a)

# 元组遍历
# a=(10,[20,30],40)
# for item in a:
#     print(item)

## 集合
'''
· Python语言提供的内置数据结构
· 与列表、字典一样都属于可变类型的序列
· 集合是没有value的字典
· 集合中的元素不允许重复，如果有会去重
'''

# 字典生成方式：
# l={'a','b','c'}
# l=set(range(6))
# l=set([9,8,7,6,5,4,3,2,1]) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# l=set((9,8,7,6,5,4,3,100)) # {3, 4, 5, 6, 7, 8, 9, 100}
# l=set('python') # {'p', 't', 'n', 'o', 'h', 'y'}
# l=set({12,13,14,15,6,5,4,3}) # {3, 4, 5, 6, 12, 13, 14, 15}
# print(l)
# print(type(l))

# 空集合
# l=set()
# print(type(l))















