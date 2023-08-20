import typer

from bl_tools.commands import r2

app = typer.Typer()
app.add_typer(r2.app, name="r2")


@app.command()
def hello_world():
    print("Hello, world!")
