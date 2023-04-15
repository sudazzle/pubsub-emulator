from google.cloud import pubsub_v1

# TODO(developer)
project_id = "test-project"
topic_id = "test-topic"

publisher = pubsub_v1.PublisherClient()

topic_path = publisher.topic_path(project_id, topic_id)

topic = publisher.create_topic(request={"name": topic_path})

print(f"Created topic: {topic.name}")