import logging
logger = logging.getLogger("events")

def publish_event(topic: str, payload: dict):
    # stub implementation: integrate with Kafka / RabbitMQ in prod
    logger.info("EVENT PUBLISH: %s %s", topic, payload)
    # TODO: hook into real event bus

from src.common.logger import logger

def emit_admin_action_logged(payload: dict):
    # In a real system this might push to Kafka / SNS. For MVP we log.
    logger.info(f"EVENT admin.action.logged: {payload}")
