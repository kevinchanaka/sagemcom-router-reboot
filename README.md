Selenium script to reboot Sagemcom F@ST 5366 TN router

## Usage

Create .env file with the following information
```
ROUTER_USERNAME=<YOUR_ROUTER_USERNAME>
ROUTER_PASSWORD=<YOUR_ROUTER_PASSWORD>
ROUTER_IP=<YOUR_ROUTER_IP>
```

Run selenium grid
```
make run-grid
```

Build and run application
```
make build
make run
```

NOTE: You can visit `localhost:7900` to view the remote browser, refer [here](https://github.com/SeleniumHQ/docker-selenium#quick-start) for more information
