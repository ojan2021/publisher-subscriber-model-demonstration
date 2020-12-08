# Publish-subscribe Communication Pattern Implementation
I wrote this program  for "Principles of Distributed Systems" course that I took in my university. This program shares the contents of the directory to the remote client with the help of "Publish-subscribe" Message Communication Pattern. I implemented this model with the help of ZeroMQ library.

### Usage
#### First we should listen to the messages of the publisher that is why start subscriber first via this command:
- `python3 subscriber.py YOUR_IP_ADDRESS PORT`
- Example: `python3 subscriber.py 192.168.1.101 8888`
#### Then, we start to publish the contents of the directory:
- `python3 publisher.py YOUR_IP_ADDRESS PORT`
- Example: `python3 publisher.py 192.168.1.101 8888`
