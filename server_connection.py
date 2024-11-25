from dotenv import load_dotenv
import os

# 加载.env文件
load_dotenv()

SERVER_IP = os.environ.get('SERVER_IP')
SERVER_PORT = os.environ.get('SERVER_PORT')

def get_server_connection():
    return (SERVER_IP, SERVER_PORT)

# 示例用法
if __name__ == "__main__":
    server_info = get_server_connection()
    print(f"Connecting to server at {SERVER_IP}
