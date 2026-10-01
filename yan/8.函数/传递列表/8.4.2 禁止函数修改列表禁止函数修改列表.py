

"""
使用[:]创建副本
"""

def verify_users(users, unconfirmed_users):
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print(f"Verifying user：{current_user.title()}")
        users.append(current_user)

def show_verified_users(users):
    print("\nThe following users have been confirmed:")
    for user in users:
        print(user.title())


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

verify_users(confirmed_users, unconfirmed_users[:])

print(f"unconfirmed_users:{show_verified_users(unconfirmed_users)}")
print(f"confirmed_users:{show_verified_users(confirmed_users)}")
