#!/bin/sh
docker build -t kleed .
mkdir -p workspace
docker run -v $(pwd)/workspace:/home/klee/workspace --rm -it kleed /bin/bash
