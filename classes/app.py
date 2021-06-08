import csv
import os
from classes.users import User

class App:
    def __init__(self):
        self.users = []
    
    def list_users(self):
        for user in self.users:
            print(f'{user.name}: {user.email}')

    def add_user(self, user_data):
        self.users.append(User(**user_data))
        self.save()
    
    def save(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/users.csv")

        with open(path, 'w') as csvfile:
            user_csv = csv.writer(csvfile, delimiter=',')
            user_csv.writerow(['name', 'email', 'drivers_license'])
            for user in self.users:
                user_csv.writerow([user.name, user.email, user.drivers_license])
            
    
