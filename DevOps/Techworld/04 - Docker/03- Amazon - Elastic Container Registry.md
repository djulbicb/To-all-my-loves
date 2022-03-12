# ElasticContainerRegistry

- Create repository in amazon, name: my-app. Specific to amazon, for each image there is a repository.
- To download from amazon, first login to docker manually or give credentials to jenkins
- Install AWS Cli, and have credentials set up
$(aws ecr get-login --no-include-email --region eu-central-1)

namin in docker registry
registryDomain/imageName:tag

for DockerHub you can use shorthand without registry domain
docker pull mongo
docker pull docker.io/library/mongo:latest

in private registry, you cant skip this part
docker pull 123456.dkr.eu-centra.amazonaws.com/my-app:latest

First tag image before pushing. Just like renaming. Pushing image pushes layers, one by one. Just like pull download one by one.
docker tag my-app:latest 123456.dkr.eu-centra.amazonaws.com/my-app:1.0
docker push 123456.dkr.eu-centra.amazonaws.com/my-app:1.0
