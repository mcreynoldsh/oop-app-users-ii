class User:
    posts = []
    def __init__(self, name, email_address, license_number):
        self.name= name
        self.email_address= email_address
        self.license_number= license_number
    
    def post(self,str):
        self.posts.append(str)

    def see_posts(self):
        view_posts = ""
        for x in self.posts:
            view_posts += f"\n{self.posts.index(x)+1}: {x}"
        return view_posts  

    def delete_post(self,post_num):
        self.posts.remove(self.posts[post_num-1])      

user_tyler = User("Tyler","tyler29@gmail.com",2345603)

user_jane = User("Jane","janejane@gmail.com",3049585)
user_tyler.post("first post")
user_tyler.post("second posts")
print(user_tyler.see_posts())
user_tyler.delete_post(2)
print(user_tyler.see_posts())