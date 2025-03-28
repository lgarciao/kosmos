import socket
from config import HOST, PORT


def start_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("No se pudo establecer una conexión con el servidor")
        return

    while True:
        message = input("Ingrese mensaje: ")
        try:
            client_socket.send(message.encode())
        except ConnectionResetError:
            print("Cerrando conexión...")
            client_socket.close()
            break

        if message == "DESCONEXION":
            print("Cerrando conexión...")
            client_socket.close()
            break

        response = client_socket.recv(1024).decode()
        print(f"Respuesta del servidor: {response}")


def main():
    start_client()


if __name__ == "__main__":
    main()
