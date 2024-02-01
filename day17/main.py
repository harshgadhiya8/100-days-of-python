class User:
    def __init__(self,id,name):
        self.id = id
        self.name = name    
        self.followers = 0
        self.following = 0
  
    def follow(self,user):
        user.followers += 1
        self.following += 1 

user1 = User('01','Harsh')
user2 = User('02','Gadhiya')
# user1.id = '01'
# user1.username = 'harsh'
user1.follow(user2)
print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)