from google.cloud.pubsub import PublisherClient
from google.cloud.pubsub_v1.types import Topic

from pubsub_emulator.constants import PROJECT_ID


class TopicRepository:
    """
    Manages the retrieval and persistence of the Pub/Sub topics.
    """

    @staticmethod
    def create(id_topic: str | None = None, request: dict | None = None) -> Topic:
        """
        Creates a new Pub/Sub topic.
        """
        if not id_topic and not request:
            raise ValueError("Either id_topic or request must be provided.")

        with PublisherClient() as publisher:
            topic_path = publisher.topic_path(PROJECT_ID, id_topic)
            return publisher.create_topic(request=request or {"name": topic_path})

    @staticmethod
    def fetch() -> list[Topic]:
        """Fetches all Pub/Sub topics"""
        with PublisherClient() as publisher:
            return publisher.list_topics(request={"project": f"projects/{PROJECT_ID}"})

    @staticmethod
    def delete(id_topic: str) -> None:
        """Deletes a Pub/Sub topic"""
        with PublisherClient() as publisher:
            topic_path = publisher.topic_path(PROJECT_ID, id_topic)
            publisher.delete_topic(request={"topic": topic_path})

    @staticmethod
    def delete_all() -> None:
        """Deletes all Pub/Sub topics"""
        with PublisherClient() as publisher:
            for topic in publisher.list_topics(request={"project": f"projects/{PROJECT_ID}"}):
                publisher.delete_topic(request={"topic": topic.name})
