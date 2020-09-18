import socket


HOST = socket.gethostname()
PORT = 9999


with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(3)

    clientsocket, address = s.accept()

    with clientsocket:

        print(f"Connection From {address} has been Established !")

        while True:
            data = clientsocket.recv(1024)
            data = data.decode("utf-8")

            if not data:
                break

            clean_data = data.split(" ")
            print(clean_data)
            number_words = len(clean_data)
            number_words = str(number_words)

            number_character = len(data)
            number_character = str(number_character)

            msg = f"{number_words} {number_character}"
            clientsocket.send(bytes(msg, "utf-8"))
