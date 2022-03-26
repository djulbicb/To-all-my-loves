kubectl get all

## Note
I am using windows. Starting up deployments lags a bit. For this example i had to start first `mongo` and then `mongo-express`. Scale deployment to 0 and then scale to 1.

## Create secret
Secret must be encoded. I used `https://www.base64encode.org/`. 

echo username | base64
echo 'password' | base64
dXNlcm5hbWU=
cGFzc3dvcmQ=

## Service

### Check if service is connected
```
kubectl describe service mongodb-service
# check endpoints in logs, compare with IP frome next command
kubectl get pods -o wide
```

- Default is ClusterIP. ClusterIP is internal IP Address. LoadBalancer gives internal and external IP address.
- When running `kubectl get services` for the first time after creating service it will show `EXTERNAL-IP <pending>`. That is because IP address wasnt assigned yet locally.
- To show IP run `minikube service mongo-express-service`
- 

```
apiVersion: v1
kind: Service
metadata:
  name: mongodb-service
spec:
  selector:
    app: mongodb
  ports:
    - protocol: TCP
      port: 27017
      targetPort: 27017
```

```
apiVersion: v1
kind: Secret
metadata:
  name: mongodb-secret
type: Opaque
data:
  mongo-root-username: LW4gJ3VzZXJuYW1lJyANCg==
  mongo-root-password: LW4gJ3Bhc3N3b3JkJyANCg==
```

```
apiVersion: v1
kind: Secret
metadata:
  name: mongodb-secret
type: Opaque
data:
  mongo-root-username: LW4gJ3VzZXJuYW1lJyANCg==
  mongo-root-password: LW4gJ3Bhc3N3b3JkJyANCg==
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongoexpress-deployment
  labels:
    app: mongoexpress
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mongoexpress
  template:
    metadata:
      labels:
        app: mongoexpress
    spec:
        contain
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongodb-deployment
  labels:
    app: mongodb
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mongodb
  template:
    metadata:
      labels:
        app: mongodb
    spec:
      containers:
        - name: mongodb
          image: mongo
          ports:
            - containerPort: 27017
          env:
            - name: MONGO_INITDB_ROOT_USERNAME
              valueFrom:
                  secretKeyRef:
                    name: mongodb-secret
                    key: mongo-root-username
            - name: MONGO_INITDB_ROOT_PASSWORD
              valueFrom:
                  secretKeyRef:
                    name: mongodb-secret
                    key: mongo-root-password
---
apiVersion: v1
kind: Service
metadata:
  name: mongodb-service
spec:
  selector:
    app: mongodb
  ports:
    - protocol: TCP
      port: 27017
      targetPort: 27017
```

