import zmq
import sys

context = zmq.Context()
s=context.socket(zmq.SUB)  # Note.
s.setsockopt_string(zmq.SUBSCRIBE, '')  # Note.

p = 'tcp://' + str(sys.argv[1]) + ':' + str(sys.argv[2])  # how and where to communicate
                                                          # (Program gets IP address and Port number from the user via commandline arguements
s.connect(p)  # connect to the server

while True:
    files = s.recv_string()     # Receiving the list of files/folders from publisher.
    print(files)
