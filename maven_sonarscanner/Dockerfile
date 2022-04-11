FROM maven:3.8.5

WORKDIR /${PROJECT_PATH}

COPY ./maven_sonarscanner/wait-for-it.sh /${PROJECT_PATH}/wait-for-it.sh

RUN chmod +x wait-for-it.sh

ENTRYPOINT [ "/bin/bash", "-c" ]
CMD ./wait-for-it.sh \
    sonarqube:9000 \
    -- \
    mvn sonar:sonar -Dsonar.projectKey=Devops-API \
    -Dsonar.host.url=http://sonarqube:9000 \
    -Dsonar.scm.provider=git \
    -Dsonar.login=admin \
    -Dsonar.password=admin
