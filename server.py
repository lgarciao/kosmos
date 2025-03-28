import socket
from config import HOST, PORT


def accept_connection(server_socket):
    conn, addr = server_socket.accept()
    print(f"Conexión establecida con {addr}")
    handle_client(conn, addr)


def handle_client(conn, addr):
    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Mensaje recibido: {data}")

            if data == "DESCONEXION":
                print("Cliente desconectado")
                break
            else:
                send_response(conn, data)
    except ConnectionResetError:
        print(f"Cliente {addr} desconectado..")
    finally:
        conn.close()


def send_response(conn, data):
    try:
        conn.send(data.upper().encode())
    except OSError:
        print("Cliente desconectado")
        conn.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Servidor TCP escuchando en el puerto {PORT}...")

    while True:
        accept_connection(server_socket)


def main():
    start_server()


if __name__ == "__main__":
    main()
