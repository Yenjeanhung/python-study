""" 字符串就是一系列字符。在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号。可使用反斜杠 \ 转义特殊字符。 """

str1 = 'this is a "string"'
str2 = "this is a 'string' too"
print(str1)
print(str2)

""" 
也可以使用三个引号表示多行字符串。三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
一个典型的用例是，当你需要一块HTML或者SQL时，使用三个引号就很简单
"""
str3 = """ hello world 
HELLO WORLD"""
print(str3)


name = "zs"
age = 20
print(name,"，年龄是：",age)



