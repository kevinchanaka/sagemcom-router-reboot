import os

ROUTER_IP = os.getenv("ROUTER_IP", "")
ROUTER_USERNAME = os.getenv("ROUTER_USERNAME")
ROUTER_PASSWORD = os.getenv("ROUTER_PASSWORD")
WAIT_TIME = int(os.getenv("WAIT_TIME", 10))
