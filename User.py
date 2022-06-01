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

person = User("Tyler","tyler29@gmail.com",2345603)

person2 = User("Jane","janejane@gmail.com",3049585)
person.post("first post")
person.post("second posts")
print(person.see_posts())
person.delete_post(2)
print(person.see_posts())