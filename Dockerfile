FROM ubuntu:latest
LABEL authors="BRIDGES"

ENTRYPOINT ["top", "-b"]