
"""

"""
def get_formatted_name(first_name, last_name, age=""):
    person = {
        "first": first_name,
        "last": last_name,
    }
    if age:
        person["age"] = age
    return person

musician = get_formatted_name("jimi", "hendrix")
print(musician)

worker = get_formatted_name("jimi", "hendrix", 32)
print(worker)