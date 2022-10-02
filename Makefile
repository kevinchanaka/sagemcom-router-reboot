-include .env
app=sagemcom-router-reboot
network=sagemcom-router-reboot

build:
	docker build -t ${app} .

run-grid:
	docker network create ${network}
	docker run --name selenium-grid -d --network ${network} \
	  -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:4.5.0-20220929

run:
	docker run --rm --network ${network} \
	  -e ROUTER_IP=${ROUTER_IP} \
	  -e ROUTER_USERNAME=${ROUTER_USERNAME} \
	  -e ROUTER_PASSWORD=${ROUTER_PASSWORD} \
	  -e WAIT_TIME=10 \
	  -e GRID_ENDPOINT=selenium-grid:4444 \
	${app}

clean:
	-docker stop selenium-grid
	-docker rm selenium-grid
	docker network rm ${network}
