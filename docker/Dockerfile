FROM alpine:latest AS builder

ENV PATH=/usr/local/bin:$PATH
RUN apk add --no-cache git build-base linux-headers cmake wget \
  swig xfce4-dev-tools \
  bash

# Download and install LEMON from source
COPY docker/install_lemon .
RUN chmod +x install_lemon && ./install_lemon

# Install boost (contains boost graph library, BGL)
COPY docker/install_bgl .
RUN chmod +x install_bgl && ./install_bgl

FROM builder as run

WORKDIR /root/
COPY . .
RUN mv docker/run . && chmod +x run
