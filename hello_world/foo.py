from aws_lambda_powertools import Logger


logger = Logger()


def foo():
    logger.warning("Logging from foo()")
    return 17
