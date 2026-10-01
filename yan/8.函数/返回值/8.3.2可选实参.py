
"""
middle_name 是可选的
"""
def get_formatted_name(first_name, last_name, moddle_name=""):
    if moddle_name:
        full_name = f"{first_name} {moddle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)


musician = get_formatted_name("jimi", "hendrix", "lee")
print(musician)