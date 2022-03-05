[61]

### Artifact
Artifact is app built into a **single file**. Its shareable and easily moweable.
### Artifact repository
Is place where artifacts are stored and needs to support that specific format
### Artifact Repository Manager
Software able to produce different types of artifacts

Common problem is having to many artifact manager. Instead of having many, you can use Artifact Repository Manager like Nexus or JFrog.
Here you can upload/store/download different build artifacts.

Nexus is a repository manager that you can use in company. Nexus can also create proxy repository to a mavenrepo to consolidate repo managment. There are also public managers like MavenRepository.
Nexus has open-source for small teams and commercial version for companies
Nexus supports LDAP for user access. Rest API for integration with other tools. When Jenkins build artifact it needs to push to nexus and then deployment server needs to fetch those artifacts to deployment server.
Back-up and restore.
Cleanup policy - remove old artifacts older than ... automatically
Support tokens as authentication for system users


```
get better droplet 

java 8
cd /opt/
wget nexus3latestunix.tar
tar -zxvf tar
# sonatype-work -contains specifc workspace configura. When update its gonna work. This can be used for backup
# nexus folder is the main one

services should not run with root user
create nexus user for service
this user only permission specific to service

adduser nexus
# create passowrd

ls -l
# two folders are for root user
nexus:nexus - this is nexus user and nexus group. Group is def created with user
chown -R nexus:nexus nexus-folder
chown -R nexus:nexus sonatype-work

vim nexus-folder/bin/nexus.rc
# service will run as user nexus. Uncomment line
#run_as_user="nexus"

# start service
su - nexus
/opt/nexus-folder/bin/nexus start
ps aux | grep nexus
netstat -lnpt # at port 8081
add to firewall inbound rule 8081
```
# def se kreira admin user sa sifrom 
in path /opt/sonatype-work/nexus/admin.password

Login as admin, crete new password, and disable for anonymus users
Zupcanik na vrhu sa configurisanje

Nexus repo
mogu biti proxy, public, host
proxy je maska za public repo
hosted sluzi za company repo, Its primary location for artifacts
snapshots are for testing
releases are actual releases

Obicno se preko LDAP importuju useri u nexus
# Upload JAR file to Nexus
1. Create user
Security > User > Crete local user. Role anonymus
2. Create Role
Security > Roles - privilidges nx-reposiotry-naven2-
privilegiju su admin i view. Izaberi view *
3. assign role to user on user view.

Add plugin to export
i maven i gradle koriste isti format za upload
```
apply plugin: 'maven-publish'
publishing {
    publications {
        maven(MavenPublication) {
            artifact("build/libs/my-app-$version"+".jar") {
                extension 'jar'
            }
        }
    }

    repository {
        maven {
            name 'nexus'
            url 'http://IP:nexusport:/repository/maven-snapshots'
            credentials {
                username project.repoUser
                password project.repoPassword
            }
        }
    }
}

repository {
    mavenCentral()
}
```
create gradle properties file
in project > new file
gradle.properties
repoUser = bojan
repoPassword = sss

settings.gradle
rootProject.name=my-app

./gradlew build

cd java-app
./gradlew publish
# publish is made available by new plugin

in nexus go to
maven>snapshots > and there is application

# For maven
<build>
    <pluginManagement>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-deploy-plugin</artifactId>
            <version>2.8.2</version>
        </plugin>
    </pluginManagement>

    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-deploy-plugin</artifactId>
        </plugin>
    </plugings>
</build>

<distributionManagment>
    <snapshotRepository>
        <id>nexus-snapshot</id>
        <url>http://IP....nexusport/maven-snapshots</url>
    </snapshotRepository>
</distributionManagment>

in .m2 folder
vim settings.xml
<settings>
    <servers>
        <id>nexus-snapshots</id>
        <username>bojan</username>
        <password>lowe</password>
    </servers>
</settings>

mvn package
mvn deploy

nexus ima api za pregled repo i components
curl user:psw -X GET 'http://555.55.555.555:8081/service/rest/v1/repositories'
curl user:psw -X GET 'http://555.55.555.555:8081/service/rest/v1/components?repository=maven-snapshots'
# for watching assets
curl user:psw -X GET 'http://555.55.555.555:8081/service/rest/v1/components/123456789id'