ARG JDK_VERSION
FROM maven:3.8.5-${JDK_VERSION}

COPY ./wait-for-it.sh /${PROJECT_PATH}/wait-for-it.sh
COPY ./entrypoint.sh /${PROJECT_PATH}/entrypoint.sh

RUN chmod +x wait-for-it.sh entrypoint.sh
