import click

from users import services
from users.models import User


@click.group()
def users():
    pass


@users.command()
@click.option('-u', '--username', type=str, prompt=True, help='Username')
@click.option('-n', '--fullname', type=str, prompt=True, help='Name')
@click.option('-e', '--email', type=str, prompt=True, help='Email')
@click.option('-p', '--phone', type=str, prompt=True, help='Phone')
def create(username, fullname, email, phone):
    user_service = services.UserService()
    all_users = user_service.list_users()

    user = [user for user in all_users if user['username'] == username]

    if user:
        click.echo('User Exist')
    else:
        user = User(username, fullname, email, phone)
        user_service.create_user(user)
        click.echo('Created user')


@users.command()
@click.option('-u', '--username', type=str, prompt=True, help='Username')
@click.confirmation_option(prompt='sure you want to delete the user?')
def delete(username):
    user_service = services.UserService()
    all_users = user_service.list_users()

    user = [user for user in all_users if user['username'] == username]

    if user:
        user_service.delete_user(username)
        click.echo("Deleted user")
    else:
        click.echo('User not found')


@users.command()
@click.option('-u', '--username', type=str, prompt=True, help='Username')
def update(username):
    user_service = services.UserService()
    all_users = user_service.list_users()

    user = [user for user in all_users if user['username'] == username]

    if user:
        user_new_values = _update_user_flow(user[0])
        user_service.update_client(username, user_new_values)
        click.echo('User updated')
    else:
        click.echo('Username not found')


def _update_user_flow(user):

    user['fullname'] = click.prompt('New Full Name', type=str, default=user['fullname'])
    user['email'] = click.prompt('New email', type=str, default=user['email'])
    user['phone'] = click.prompt('New Phone', type=str, default=user['phone'])

    return user


@users.command()
def tolist():
    user_service = services.UserService()
    all_users = user_service.list_users()

    click.echo("UID | Username | Fullname | Emial | Phone")
    for user in all_users:
        click.echo("{uid} | {username} | {fullname} | {email} | {phone}".format(
            uid=user['_id'],
            username=user['username'],
            fullname=user['fullname'],
            email=user['email'],
            phone=user['phone']
        ))


all_commends = users
