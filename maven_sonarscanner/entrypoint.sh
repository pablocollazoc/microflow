#!/bin/bash

/wait-for-it.sh sonarqube:9000 --strict -- \
    curl -X POST -d "name=custom" http://sonarqube:9000/api/qualitygates/create
    mvn clean verify -DskipTests sonar:sonar -Dsonar.projectKey=Devops-API -Dsonar.host.url=http://sonarqube:9000 -Dsonar.scm.provider=git -Dsonar.login=admin -Dsonar.password=admin
