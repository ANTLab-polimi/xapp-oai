FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    git \
    python3.8 \
    python3-pip \
    protobuf-compiler

# install protobuf python module
RUN python3 -m pip install protobuf==3.20.*

COPY . /xapp-oai
WORKDIR /xapp-oai

# synch submodules
RUN chmod +x submodule-sync.sh
RUN ./submodule-sync.sh

ENTRYPOINT ["/bin/bash"]
