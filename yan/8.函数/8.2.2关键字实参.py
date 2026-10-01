

# 基于名称将值进行关联，函数不会混淆

def describe_pet(animal_type, animal_name):

    print(f"\nI have a {animal_type}")

    print(f"My {animal_type}'s name is {animal_name}")


describe_pet(animal_name="harry", animal_type="hamster")

describe_pet(animal_type="cat", animal_name="tom")