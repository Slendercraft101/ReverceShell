import requests

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        ip_info = response.json()
        return ip_info["ip"]
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving public IP: {e}")
        return None

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        print(f"Your public IP address is: {public_ip}")
    input("Press Enter to exit...")
