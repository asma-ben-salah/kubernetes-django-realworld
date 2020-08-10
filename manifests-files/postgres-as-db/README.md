
## Environment

All Kubernetes files except **Postgres** are deployable on both Minikube and RKE cluster.The only difference is when creating Postgres statefulset.

With RKE cluster I am using dynamic provisioning with vSphere as cloud provider. 

However, with minikube it is a persistent volume with type hostPath (a local file system)


## DataBase and persisting Data

The django realworld example app, use Sqlite as DataBase which not production , I switch to PostgreSQL.

The changes are:

Edit the conduit/setting.py to change the DATABASES section

```JSON
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'default',
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT', 5432)
     }
}
```

## Readiness 

I setup a health check endpoint to checks for database connection, which will serve as readiness HTTP request. for more details checks [the code](../../app/conduit/apps/health-check/views.py)

## Django Migration 

The migration.yml run the Django migrations to set up the application models.

## Exposition Application

* For Minikube a  service with type NodePort
* RKE use Inginx as Ingres Controller, so I create a

## Run application
In order to run the application, you to 
* Create the namespace: 
* Setup postres credentials 
* Deploy Postgres
* Run django migration
* Run django deployment
* Expose DataBase
* to activate autoscaling :
```shell
kubectl apply -f namespace.yml
kubectl apply -f secret.yml
kubectl apply -f postgres-stateful-minikube.yml / postgres-stateful-minikube.yml
kubectl apply -f migration-job.yml

kubectl apply -f deployment.yml
kubectl apply -f service.yml
kubectl apply -f ingress.yml
```