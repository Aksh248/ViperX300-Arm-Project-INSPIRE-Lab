import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5678")  # Replace 'localhost:5555' with the address of the server

# Define coordinate values
x = 10
y = 20

# Send coordinate values to the server
data = {'x': x, 'y': y}
socket.send_json(data)

# Receive the result from the server
response = socket.recv_json()
result = response['result']
print('Result:', result)

