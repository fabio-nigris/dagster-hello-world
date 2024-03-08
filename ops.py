from dagster import op

@op
def hello_world():
    return 'Hello, World!'