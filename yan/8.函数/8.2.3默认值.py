
"""
在编写函数时，可以给每个形参指定默认值当函数描述的动物大多是小狗时，我们将 animal_type 默认值设置为 'dog
Python 要求没有默认值的参数必须放在有默认值的参数之前。
"""
def describe_pet(animal_name, animal_type="dog"):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {animal_name}")

describe_pet(animal_name="harry")

describe_pet(animal_name="tom", animal_type="cat")

describe_pet("jerry", "mouse")
