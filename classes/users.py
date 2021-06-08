import csv
import os
from classes.post import Post

class User:
    def __init__(self, name, email, drivers_license):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license
        self.posts = []
    
    def create_post(self, post_object):
        self.posts.append(Post(**post_object))
        self.save()
    
    def save(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/posts.csv")

        with open(path, 'w') as csvfile:
            post_csv = csv.writer(csvfile, delimiter=',')
            post_csv.writerow(['title', 'content'])
            for post in self.posts:
                post_csv.writerow([post.title, post.content])



    
