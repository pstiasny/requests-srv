#!/bin/bash
set -euo pipefail

function cleanup() {
    echo cleaning up
    docker rm -f $CONSUL $HTTPD
}

trap cleanup EXIT
CONSUL=$( docker run -h test-node --dns 127.0.0.1 -d progrium/consul -server -bootstrap -advertise 127.0.0.1 )
HTTPD=$( docker run --net "container:$CONSUL" -d nginx )
docker build -t requests-srv-test . &&
docker run --rm --net "container:$CONSUL" -ti requests-srv-test py.test
