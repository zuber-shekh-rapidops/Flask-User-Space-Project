from userspaceapp import db
from userspaceapp.users.models import User,Post

users=User.query.all()
for user in users:
    print(f"{user.email}|{user.password}|{user.posts}")
    for post in user.posts:
        print(post.title)

