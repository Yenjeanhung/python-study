
""" 我们有时候需要接受任意数量的实参，但不知道信息是什么样的，例如用户会希望使用一些自定义信息来创建账户，此时可以： """

def build_profile(first, last, **user_info): 
    """创建一个字典，其中包含我们知道的有关用户的一切""" 
    user_info['first_name'] = first 
    user_info['last_name'] = last 
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)