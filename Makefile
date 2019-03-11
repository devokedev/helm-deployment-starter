SHELL=/bin/bash

SCRIPTS_PATH=./scripts

init:
	python3 ${SCRIPTS_PATH}/init.py -n app-${ENV}

set-default-namespace:
	kubectl config set-context $(shell kubectl config current-context) --namespace=${NSPACE}

app1-up:
	python3 ${SCRIPTS_PATH}/up.py -n appone -c App1

app2-up:
	python3 ${SCRIPTS_PATH}/up.py -n apptwo -c App2

app1-down:
	python3 ${SCRIPTS_PATH}/down.py appone

app2-down:
	python3 ${SCRIPTS_PATH}/down.py apptwo

up: app1-up app2-up 

down: app1-down app2-down

list-charts:
	helm ls --all

upgrade-app-1:
	helm upgrade appone ./App1

upgrade-app-2:
	helm upgrade apptwo ./App2
