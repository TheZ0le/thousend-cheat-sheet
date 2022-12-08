from pywebio import start_server
from pywebio import config

from manager import main


config(theme="dark")


# Starting the Script
if __name__ == "__main__":
    start_server(main, port=8084, debug=True)
