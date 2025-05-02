import socket
import threading
import pickle

HOST = '0.0.0.0'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
positions = {}

def handle_client(conn, addr, player_id):
    global positions
    print(f"Connected by {addr}")
    conn.send(pickle.dumps(player_id))

    while True:
        try:
            data = pickle.loads(conn.recv(1024))
            positions[player_id] = data
            conn.send(pickle.dumps(positions))
        except:
            break

    conn.close()

def main():
    print("Server is running...")
    player_id = 0
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        threading.Thread(target=handle_client, args=(conn, addr, player_id)).start()
        player_id += 1

if __name__ == "__main__":
    main()
