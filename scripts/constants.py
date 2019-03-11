#!/usr/bin/env python

CREATE_NAMESPACE = 'kubectl create namespace {}'
DELETE_PACKAGE = 'helm del --purge {}'
INSTALL_PACKAGE = 'helm install --name {name} ./{chart}'
UPGRADE_PACKAGE = 'helm upgrade {}'
REGISTRY_SECRET = 'kubectl create secret docker-registry {secret_name} \
    --docker-server={docker-server} \
    --docker-username={docker-username} \
    --docker-password={docker-password} \
    --docker-email={docker-email}'
CREATE_SECRET = 'kubectl create -f {}'
SET_DEFAULT_NAMESPACE = 'kubectl config set-context $(kubectl config current-context) --namespace={}'

IMAGE_PULL_SECRET = 'regcred'
DEFAULT_REGISTRY_SERVER = 'https://registry.gitlab.com'
