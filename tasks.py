from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/app.py")

@task
def init(ctx):
    ctx.run("python3 src/init_db.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage-report(ctx):
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage html")

