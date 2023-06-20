import yaml
import sys
import base64

def main():
    if(len(sys.argv) <= 1):
        raise Exception("Input error. 1 input is expected by the script which should be file location.")
    file_location = sys.argv[1]

    with open(file_location, 'r') as text_file:
        secret_data = yaml.safe_load(text_file)
    
    data: dict = secret_data['data']

    for key in data.keys():
        key_data: str = data[key]
        decoded_key_data: str = base64.b64decode(key_data).decode()
        with open(key, 'w') as write_file:
            write_file.write(decoded_key_data)

main()