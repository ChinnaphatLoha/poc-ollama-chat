import click
from .client import OllamaClient
from .config import load_config


@click.group()
def cli():
    """CLI for chatting with gemma"""
    pass


@cli.command()
@click.option('--prompt', '-p', prompt=True, help='Prompt string to send')
def chat(prompt):
    """Send a single prompt and receive response."""
    cfg = load_config()
    client = OllamaClient(model=cfg["model"])
    response = client.query(prompt=prompt)
    click.echo(response)


if __name__ == '__main__':
    cli()
