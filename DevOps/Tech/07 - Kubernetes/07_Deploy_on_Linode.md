# Linode
Bar > Create > Kubernetes
Cluster label: test
Region: Frankfurt
Kubernetes version: latest 1.17
Choose nodes: Shared CPU 4GB 
This service created master node and you only pick worker nodes
Create Cluster

# Deploying
Options are:
1. Create own config files
2. Use bundle of those configs (Better this one)

Search for helm mongo
export KUBECONFIG=test-kubeconfig.yaml
kubectl get node
helm repo add bitnami https://charts.bitnami.com/bintnami
helm search repo bitnami
helm search repo bitnami/mongo

# pogledaj koji parametri su available
```
architecture: replicaset for multiple replicas. or standalone
auth.rootPassword
volume: use StorageClass of Linode Cloud Storage
```

test-mongodb.yaml
```
architecture: replicaset
replicaCount: 3
persistence: 
    storageClass: "linode-block-storage"
auth:
    rootPassword: secret-root-pwd
```
install chart
```
helm install arbitraryNameMongoDb --values test-mongo.yaml bitnami/mongodb
helm install [our name] --values [values file name] [chart name]
kubectl get all
kubectl get secret
```

By default for each pod a persistent volume is created

# Deploy mongo-express
own config cause only one container and service
```
apiVersion: apps/v1
kind: Deployment
metadata:
    name: mongo-express
    labels:
        app: mongo-express
spec:
    replicas: 1
    selector:
        matchLabels:
            app: mongo-express
     template:
        metadata:
            labels:
                app: mongo-express
        spec:
            containers:
            - name: mongo-express
              image: mongo-express
              ports:
              - containerPort: 8081
              env: 
              - name: ME_CONFIG_MONGODB_ADMINUSERNAME
                value: root
              - name: ME_CONFIG_MONGODB_SERVER
                value: mongodb-0.mongodb-headless
              - name: ME_CONFIG_MONGODB_ADMINPASSWORD
                valueFrom:
                    secretKeyRef:
                        name: mongodb
                        key: mongodb-root-password
---
apiVersion: v1
kind: Service
metadata:
    name: mongp-express-service
spec:
    selector:
        app: mongo-express
    ports:
        - protocol: TCP
          port: 8081
          targetPort: 8081    
    
``` 

kubectl get secret mongodb -o yaml
this is the pod endpoint `mongodb-0.mongodb-headless` where to connect

kubectl apply -f test-mongo-express.yaml
kubectl get pod
kubectl logs <hash> to see if connected

Mongo express is internal service so we need to configure ingress controller
## Deploy ingress controller
We can use helm.

helm repo add stable https://kubernetes-charts.storage.googleapis.com
# outdated
helm install nging-ingress stable/nginx-ingress --set controller.publishService.enabled=True
kubectl get pod

Go to Linode> NodeBalancer : On je default kreiran 
On prosledjuje Ingresu pa servisu

kubectl gets svc `service je kreiran LoadBalancer`
Host mora da bude url ne moze IP. Get host name from nodebalancers view
```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
    annotations:
        kubernetes.io/ingress.class: nginx
    name: mongo-express
spec:
    rules:
        - host: nb-139-162-140-213.frankfurt.nodebalancer.linode.com
          http:
            paths:
                - path: /
                  backend: 
                    serviceName: mongo-express-service
                    servicePort: 8081
```
kubectl apply -f test-ingress.yaml
go to that url in host

# Delete pods and recreate
kubectl scale --replicas=0 statefulset/mongodb
kubectl scale --replicas=3 statefulset/mongodb
volumes are first unattached and then reattached

helm ls
helm uninstall mongodb
# Delete
Dashboard sidebar > Kubernetres > Delete cluster
