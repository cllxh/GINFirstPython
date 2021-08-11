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

#a=1
#b=input('请输入数字')
#print(int(b)-a)

# ctrl+/ 快速注释































































