import json
import logging

from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.api_gateway import ALBResolver, Response

powertools_logger = Logger()
actual_logger = logging.getLogger(powertools_logger.service)

app = ALBResolver()


def handler(event, context):
    return app.resolve(event, context)


@app.get("/log-test")
def lambda_handler(event, context):

    print(f"powertools_logger level = {powertools_logger.getEffectiveLevel()}")
    print(f"actual_logger level = {actual_logger.getEffectiveLevel()}")

    powertools_logger.info("info-level log output")
    powertools_logger.debug("debug-level log output")   # no output

    powertools_logger.setLevel("DEBUG")
    print(f"powertools_logger level = {powertools_logger.getEffectiveLevel()}")
    print(f"actual_logger level = {actual_logger.getEffectiveLevel()}")

    powertools_logger.info("info-level log output 2")
    powertools_logger.debug("debug-level log output 2")   # no output

    actual_logger.setLevel("DEBUG")
    print(f"powertools_logger level = {powertools_logger.getEffectiveLevel()}")
    print(f"actual_logger level = {actual_logger.getEffectiveLevel()}")

    powertools_logger.info("info-level log output 3")
    powertools_logger.debug("debug-level log output 3")   # yes output

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"hello world!"
        })
    }

