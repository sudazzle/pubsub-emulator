import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from google.cloud import pubsub_v1
import argparse
import os

parser = argparse.ArgumentParser(description='Process some integers.', prog="test one")
parser.add_argument('--push_endpoint', '-p')
parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag
args = parser.parse_args()

# Setup pup sub
project_id = "test-chat-app"
subscription_id = "test-subscription-id"
topic_id = "messages"

if 'PUSH_ENDPOINT' in os.environ or args.push_endpoint:
  push_subscription_endpoint = args.push_endpoint or os.environ['PUSH_ENDPOINT']
else:
  print('Either PUSH_ENDPOINT environment variable or --push_endpoint argument option required')
  exit()

#  "http://host.docker.internal:3333"
publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()
topic_path = publisher.topic_path(project_id, topic_id)
subscription_path = subscriber.subscription_path(project_id, subscription_id)

push_config = pubsub_v1.types.PushConfig(push_endpoint=push_subscription_endpoint)



# HTTPRequestHandler class
class HTTPRequestHandler(BaseHTTPRequestHandler):
  # GET
  def do_POST(self):
    if self.path == '/send-message':
      content_length = int(self.headers['Content-Length'])
      post_data = json.loads(self.rfile.read(content_length))
      post_str = json.dumps(post_data)
      # Data must be a bytestring
      data = post_str.encode('utf-8')
      publisher.publish(topic_path, data)
      self.send_response(201)

#main
def main():
  try:
    try:
      publisher.create_topic(request={"name": topic_path})

      with subscriber:
        subscription = subscriber.create_subscription(
          request={
            "name": subscription_path,
            "topic": topic_path,
            "push_config": push_config
          }
        )
    except:
      print("Topic already created %s" % topic_id)

    # set up server
    PORT = 8000
    server = HTTPServer(('', PORT), HTTPRequestHandler)
    print('Started HTTP server on port ', PORT)

    # wait forever for incoming http requests
    server.serve_forever()
  except Exception as inst:
    print(inst)


if __name__ == '__main__':
  main()