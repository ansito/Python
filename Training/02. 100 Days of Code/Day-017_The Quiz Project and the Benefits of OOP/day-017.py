# Day 17: The Quiz Project

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0         # default attributes
        self.following = 0

    # adding methods to the class
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "andar")
print(user_1.id)

user_2 = User("002", "nella")
print(user_2.id)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
