import socket
from config import HOST, PORT


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Servidor TCP escuchando en el puerto {PORT}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Conexión establecida con {addr}")

        while True:
            try:
                data = conn.recv(1024).decode()
            except ConnectionResetError:
                print(f"Cliente {addr} desconectado..")
                conn.close()
            if not data:
                break
            print(f"Mensaje recibido: {data}")

            if data == "DESCONEXION":
                print("Cliente desconectado")
                conn.close()
                break
            else:
                try:
                    conn.send(data.upper().encode())
                except OSError:
                    print("Cliente desconectado")
                    conn.close()
                    break


def main():
    start_server()


if __name__ == "__main__":
    main()
