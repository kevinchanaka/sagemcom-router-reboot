import os

ROUTER_IP = os.getenv("ROUTER_IP", "")
ROUTER_USERNAME = os.getenv("ROUTER_USERNAME")
ROUTER_PASSWORD = os.getenv("ROUTER_PASSWORD")
GRID_ENDPOINT = os.getenv("GRID_ENDPOINT", "127.0.0.1:4444")
WAIT_TIME = int(os.getenv("WAIT_TIME", 10))
