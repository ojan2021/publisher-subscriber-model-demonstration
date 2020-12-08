import zmq
import sys

context = zmq.Context()
s = context.socket(zmq.SUB)
s.setsockopt_string(zmq.SUBSCRIBE, 'Folder')  # We subscribe to the messages that contain Folder word.
s.subscribe('\n')

p = 'tcp://' + str(sys.argv[1]) + ':' + str(sys.argv[2])  # How and Where to communicate
                                                          # (Program gets IP address and Port number from the user via commandline arguements
s.connect(p)  # Connect to the publisher

while True:
    files = s.recv_string()     # Receiving the list of files/folders from publisher.
    print(files)