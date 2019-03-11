# Application Cluster Module

## Getting Started

### Setup

- ```make init ENV=<dev/prod/staging>```
```
- Creates a new namespace for the mentioned environment with the name app-<env>.

- Creates a new secret for pulling private registry images with the name regcred. Will ask you for username, email and password.

```

- ```make up```
```
Starts App1 and App2 helm package.
```

### Shutdown

```make down```
```
Deletes App1 and App2 helm package.
```

### Directory Structure

```
.
├── App1
│   ├── Chart.yaml
│   ├── templates
│   │   ├── configmap.yml
│   │   ├── deployment.yaml
│   │   ├── helpers.tpl
│   │   ├── ingress.yaml
│   │   ├── NOTES.txt
│   │   ├── secret.yml
│   │   └── service.yaml
│   └── values.yaml
├── App2
│   ├── Chart.yaml
│   ├── templates
│   │   ├── configmap.yml
│   │   ├── deployment.yaml
│   │   ├── helpers.tpl
│   │   ├── ingress.yaml
│   │   ├── NOTES.txt
│   │   ├── secret.yml
│   │   └── service.yaml
│   └── values.yaml
├── Cheatsheet.md
├── Makefile
├── README.md
└── scripts
    ├── constants.py
    ├── down.py
    ├── init.py
    └── up.py
```