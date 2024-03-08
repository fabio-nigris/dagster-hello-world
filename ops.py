from dagster import op, In, Nothing, OpExecutionContext

@op
def hello_world_1(context: OpExecutionContext):
    context.log.info('Hello, World 1!')

@op(ins={"start": In(Nothing)})
def hello_world_2(context: OpExecutionContext):
    context.log.info('Hello, World 2!')

