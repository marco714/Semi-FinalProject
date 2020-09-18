import socket

HOST = socket.gethostname()
PORT = 9999

client_input = input("What Do you want to input: ? ")

with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(bytes(client_input, "utf-8"))

    length_data = s.recv(1024)
    length_data = length_data.decode("utf-8")

    print(f"The Length of Input is {length_data}")
