import click
from models.user import User
@click.command()
@click.argument('user', nargs=-1)
def create_user(user):
    name= user[0]
    password = password[1]
    if name and password:
        obj = User(username=name,password=password)
        obj.save()
        return click.echo("User created successfull")
    return click.echo("something is wrong")

@click.command()
@click.argument('login', nargs=-1)
def login_user(login):
    username= login[0]
    password = login[1]
    if username and password:
        obj = User.object(username=username,password=password)
        if obj[0]:
            return "user is successfully verify"
        return "something is wrong"
