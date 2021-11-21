from invoke import task

@task
def start(ctx):
    try:
        ctx.run("python src/app.py")
    except:
        ctx.run("python3 src/app.py")

@task
def init(ctx):
    try:
        ctx.run("python src/init_db.py")
    except:
        ctx.run("python3 src/init_db.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage html")

