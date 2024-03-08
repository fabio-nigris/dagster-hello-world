from dagster import job

from ops import hello_world_1, hello_world_2

@job
def hello_world_job():
    start = hello_world_1()
    hello_world_2(start=start)