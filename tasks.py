from pathlib import Path

from invoke.tasks import task


def sources() -> str:
    return " ".join(map(str, list(Path("src").rglob("*.py"))))


@task
def update(c):
    c.run("pip-compile requirements.in")
    c.run("pip install -r requirements.txt")
    c.run("pip install -r dev-requirements.txt")


@task
def format(c):
    c.run(f"black {sources()} tasks.py")
    c.run(f"isort {sources()} tasks.py")


@task
def lint(c):
    c.run(f"ruff {sources()}")
    c.run(f"mypy {sources()}")


@task
def fix(c):
    c.run(f"ruff {sources()} --fix")
