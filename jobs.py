from dagster import job

from ops import hello_world

@job
def hello_world_job():
    hello_world()