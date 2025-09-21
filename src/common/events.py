import logging
logger = logging.getLogger("events")

def publish_event(topic: str, payload: dict):
    # stub implementation: integrate with Kafka / RabbitMQ in prod
    logger.info("EVENT PUBLISH: %s %s", topic, payload)
    # TODO: hook into real event bus
