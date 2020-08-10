

# kubernetes-django-realworld

This project walks you through how to deploy a [Django Real World Example App] (https://github.com/gothinkster/django-realworld-example-app) on kubernetes Cluster.

This repository contains:

* app: the source code and Dockerfile for the application.
* manifests-files: set of YAML files that deploy the application on Kubernetes cluster.

## Build Docker Image
To build docker image, 
```Shell
cd app
docker build . -t django-realworld-example-app:tag
```
## Requirements

All Kubernetes manifest files are tested against [Rancher Kubernetes Engine](https://rancher.com/docs/rke/latest/en/) (RKE) and minikube.

Here the software version:

| Software      | Second Header |
| ------------- | ------------- |
| Docker        | 19.03.11      |
| Kubernetes    | 1.17.6        |
| Minikube      | 1.12.2        |
| Rke           | 1.1.2         |

## Run application

To deploy application using Sqlite as database, run the following command:

```Shell
kubectl apply -R -f ./sqlite3-as-db/

```

else for PostgreSQL check the [README file](manifests-files/postgres-as-db/README.md)

!!! note
    If you choose to deploy the application with sqlite, don't forget to run `kubectl exec <pod_name> -- python /app/manage.py migrate`. Else with postgres the migration is included in the manifests.



