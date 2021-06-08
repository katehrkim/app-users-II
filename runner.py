from classes.app import App
from classes.users import User

test = App()
test.list_users()
user_one = {'name':'kate'}
user_one['email'] = 'katekim@gmail.com'
user_one['drivers_license'] = 'none'
test.add_user(user_one)
test.list_users()
post_one = {'title':'hello'}
post_one['content'] = 'hello from the other side'
test.users[0].create_post(post_one)