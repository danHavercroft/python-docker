import requests
from time import sleep

def get_ip() -> str:
    # GET request to icanhazip.com
    try:
        response = requests.get("https://icanhazip.com")
    except:
        return ("Error getting IP.")

    if response.status_code != 200:
        return (f"Request failed with code {response.status_code}")
    else:
        return response.text
    

if __name__ == "__main__":
    print("Starting IP Checker...")
    
    while True:
        print(get_ip())
        sleep(5)