import zmq

context = zmq.Context()
s=context.socket(zmq.SUB)  # Note.
s.setsockopt_string(zmq.SUBSCRIBE, '')  # Note.

p = 'tcp://' + '192.168.0.105' + ':' + '8888'  # how and where to communicate
s.connect(p)  # connect to the server

while True:  # Five iterations
    files = s.recv_string()
    print(files)
