# Heml
- Package Manager for Kubernetes. Like apt yum brew for k8s. 
- A way to package yaml files and distribute them through repositories
- Bundle of Yaml files
- Reuse configuration

For example to deploy Elastic Logging you need to create StatefulSet, ConfigMap, k8s User with permissions, secret, services...
Elastic Stack deployment is the standard so someone created helm files once, packaged them and deployed.

Find chart like this
```
helm search <keyward>
HelmHub
HelmChars
```

Helm is also a templating engine. Lets say you have a cluster of microservices.
Deployment and Service are almost the same, but the only thing that is different is application name and version.
1. Define common bluepring for all microservices
2. Dynamic value replaced by placeholders with template file

```
metadata:
    name: {{.Values.name}}
    
# values.yaml
name: my-app
container:
    name: my-app-cont
    image: my-app-image
    port: 9001
```

## Chart directory
Prilikom instalacije mogu da se definisu override values. U tom slucaju kreira se merge objekat oba values file 
```
mychart/                # name of the chart
    Chart.yaml          # contains meta information about chart. name version dependencies
    values.yaml         # place for values in template files. These are default values
    charts/             # charts dependencies. If it depends on other charts
    templates/          # Template files are installed here. 
    
heml install <chartname>
heml install --values=my-override-values.yaml <chartname>
helm install --set version=2.0.0
```

## Release Management
Postoji helm 2 i 3. U 2 postoji Tiller koji je bio zaduzen da u k8s clusteru kreira podove.
Tiller je takodje radio version history za rollback. Problem je sto je Tiller imao previse permissiona, big security issue.
Pa je helm 3 izbacio Tiller i generise binary files.
```
helm install <helmname>
helm upgrade <helmname>
helm rollback <helmname>
```