import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")  # Replace 'localhost:5555' with the address of the server

try:
    # Define data value
    data = 10
    
    # Send data value to the server
    socket.send_json({'data': data})
    
    # Receive the result from the server
    response = socket.recv_json()
    result = response['result']
    print('Result:', result)
finally:
    # Close the socket when done
    socket.close()
    context.term()
