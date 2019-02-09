import click

from users.commands import all_commends as users_commends


@click.group()
def cli():
    pass


cli.add_command(users_commends)
