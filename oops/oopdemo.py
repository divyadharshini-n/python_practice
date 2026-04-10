from user import User

user1 = User("Dhianesh","abcd123")
user2 = User("Divya","abcde12345")

user1.register()
user1.login()
print(user1.user_name)
print(user1.pwd)
print(User.users)