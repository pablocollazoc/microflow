#!/bin/bash
/wait-for-it.sh sonarqube:9000 --strict -- \
    sleep 30
    curl -X POST -u admin:admin -d "name=custom" http://sonarqube:9000/api/qualitygates/create
    curl -X POST -u admin:admin -d "name=custom" http://sonarqube:9000/api/qualitygates/set_as_default
    curl -X POST -u admin:admin -d "gateName=custom&metric=coverage&op=LT&error=80" http://sonarqube:9000/api/qualitygates/create_condition
    curl -X POST -u admin:admin -d "gateName=custom&metric=duplicated_lines_density&op=GT&error=3" http://sonarqube:9000/api/qualitygates/create_condition
    curl -X POST -u admin:admin -d "gateName=custom&metric=sqale_rating&op=GT&error=1" http://sonarqube:9000/api/qualitygates/create_condition
    curl -X POST -u admin:admin -d "gateName=custom&metric=reliability_rating&op=GT&error=1" http://sonarqube:9000/api/qualitygates/create_condition
    curl -X POST -u admin:admin -d "gateName=custom&metric=security_rating&op=GT&error=1" http://sonarqube:9000/api/qualitygates/create_condition
    curl -X POST -u admin:admin -d "gateName=custom&metric=security_hotspots_reviewed&op=LT&error=100" http://sonarqube:9000/api/qualitygates/create_condition
    mvn clean verify -DskipTests sonar:sonar -Dsonar.projectKey=project -Dsonar.host.url=http://sonarqube:9000 -Dsonar.scm.provider=git -Dsonar.login=admin -Dsonar.password=admin
