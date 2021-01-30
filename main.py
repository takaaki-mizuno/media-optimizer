import click
from media_optimizer import OptimizeCommand, StatusCommand


@click.group()
def main():
    pass


@click.command()
@click.argument('path')
def optimize(path):
    OptimizeCommand().optimize(path)


@click.command()
def status():
    StatusCommand().get_status()


main.add_command(optimize)
main.add_command(status)

if __name__ == '__main__':
    main()
