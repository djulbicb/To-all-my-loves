# Jenkins versioning using Maven

Working with versions in different build tools
```
# maven - pom.xml
<version>1.5.0</version>

# node - package.json
{
        "name": "my-project",
        "version": "1.5.0",
        ...
}

# gradle - build.gradle
group = 'com.github.jitpack'
version = '1.5.0'
```

# Versions
```
4.2.1
4 - major - Breaking changes, not backward compatible
2 - minor - Minor version, but backward comaptible. API features
1 - patch - Minor changes and bug fixes. Doesnt change API
```

# Update Maven version programmatically
Uses plugin `build-helper`. This command doesnt work in this form on Windows terminal. I used linux terminal emulator on windows `CMDER` to run this command in project. 
```
# plugin available for mvn. Parses version in pom file
mvn build-helper:parse-version versions:set -DnewVersion="${parsedVersion.majorVersion}.${parsedVersion.minorVersion}.${parsedVersion.nextIncrementalVersion}" versions:commit 
 
[property].majorVersion
[property].minorVersion
[property].incrementalVersion

[property].nextMajorVersion
[property].nextMinorVersion
[property].nextIncrementalVersion

versions:commit ce updejtovati pom.xml
```

# Create Git token
Commiting with url encoded credentials is not supported anymore. Need to create a git token and use that instead.
```
# This used to work, but not anymore
withCredentials([usernamePassword(credentialsId: 'example-secure', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
            def encodedPassword = URLEncoder.encode("$GIT_PASSWORD",'UTF-8')
            sh "git config user.email admin@example.com"
            sh "git config user.name example"
            sh "git add ."
            sh "git commit -m 'Triggered Build: ${env.BUILD_NUMBER}'"
            sh "git push https://${GIT_USERNAME}:${encodedPassword}@github.com/${GIT_USERNAME}/example.git"
        }
```
![](img/04_10_cant_commit_with_url_encoded.png)

To create a new git token, go to
> Git > Settings > Developer Settings (Last option in sidebar) > Personal Access token > Generate new token
![](img/04_11_create_git_token.png)
On next screen for access privilidges pick: repo, admin:org
 
# Jenkinsfile
During build we used $BUILD_NUMBER to get the number id of jenkins job and create unique image name. 
```
#!/usr/bin/env.groovy
pipeline {
    agent any
    tools {
        maven 'maven-installation'
    }
    stages {
        stage('increment version') {
            steps {
                script {
                    echo "Incrementing app version..."
                    sh "mvn build-helper:parse-version versions:set -DnewVersion=\\\${parsedVersion.majorVersion}.\\\${parsedVersion.minorVersion}.\\\${parsedVersion.nextIncrementalVersion}-SNAPSHOT versions:commit"
                    def matcher = readFile('pom.xml') =~ '<version>(.*)</version>'
                    def version = matcher[0][1]
                    matcher = null // throws exception Not seriazable regex. This cuts the link between

                    IMAGE_VERSION = "${version}-${BUILD_NUMBER}"
                    echo "version name is ${IMAGE_VERSION}"
                }
            }
        }
        stage('build app') {
            steps {
                script {
                    echo "Building the application...${IMAGE_VERSION}"
                    sh "mvn clean package"
                }
            }
        }
        stage('build image') {
            steps {
                script {
                    echo "Building the application..."
                    withCredentials([usernamePassword(credentialsId: 'docker-hub', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                        sh "docker build -t djulb/echo4j:$IMAGE_VERSION ."
                        sh "echo $PASS | docker login -u $USER --password-stdin"
                        sh "docker push djulb/echo4j:$IMAGE_VERSION"
                    }
                }
            }
        }
        stage("deploy") {
            steps{
                script{
                    echo "deploying docker image to EC2..."
                }
            }
        }
        stage("Version bump") {
            steps{
                script{
                    // Created token as username as credentials
                    withCredentials([usernamePassword(credentialsId: 'gitwithtoken', passwordVariable: 'GIT_TOKEN', usernameVariable: 'GIT_USERNAME')]) {
                        //  For github:  https://stackoverflow.com/questions/19922435/how-to-push-changes-to-github-after-jenkins-build-completes
                        // def encodedPassword = URLEncoder.encode("$GIT_PASSWORD",'UTF-8')
                        sh "git config user.email djulb@example.com"
                        sh "git config user.name djulbicb"
                        sh "git add ."
                        sh "git commit -m 'Triggered Build: ${env.BUILD_NUMBER}'"
                        sh "git remote set-url origin https://${GIT_TOKEN}@github.com/${GIT_USERNAME}/echo4j.git"
                        sh "git push origin HEAD:maven-versioning"
                    }
                }
            }
        }
    }
}
```
**Dockerfile**
Modify Dockerfile to use regex * instead of hardcoded version. 
Instead of `ENTRYPOINT` use `CMD` cause it support regex.
When using regex its important to have only one jar file in target folder, so use `mvn clean package` command.
```
FROM openjdk:8-jre-alpine
EXPOSE 8080
COPY ./target/echo-*.jar /usr/app/echo.jar
WORKDIR /usr/app
CMD java -jar echo-*.jar
```

**pom.xml**
```
	<build>
		<pluginManagement>
			<plugins>
				<plugin>
					<groupId>org.apache.maven.plugins</groupId>
					<artifactId>maven-deploy-plugin</artifactId>
					<version>2.8.2</version>
				</plugin>
			</plugins>
		</pluginManagement>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>

			<plugin>
				<groupId>org.sonatype.plugins</groupId>
				<artifactId>nexus-staging-maven-plugin</artifactId>
				<version>1.6.3</version>
				<extensions>true</extensions>
			</plugin>
		</plugins>
	</build>
```

# Commit version change to github
If you are using webhooks make sure to tell jenkins to skip the build once version is commited back to github. Cause it will cause infinite loop of builds.

For this install plugin jenkins `ignore committer strategy`

Go to multibranch project and there is an option in branch source panel to ignore commit based on email of user.

# Additionaly, remove target folder for commit, to make it slim
```
.gitignore
.idea/*
target
git rm -r --cached target
git add .
git commit -m "remove target folder from repo"
git pull
git push
```


