import click

from users.commands import all_commends as users_commends

DB_NAME = 'escuela3d'


@click.group()
@click.pass_context
def cli(ctx):
    """ Commandline App """

    ctx.obj = dict()
    ctx.obj['database'] = {
        "db_client": "mongodb://localhost:27017",
        "db_name": "escuela3d"
    }


cli.add_command(users_commends)
