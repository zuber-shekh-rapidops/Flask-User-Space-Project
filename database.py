from userspaceapp import db
from userspaceapp.users.models import User

users=User.query.all()

for user in users:
    print(f"{user.email}|{user.password}")