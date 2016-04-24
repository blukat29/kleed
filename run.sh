#!/bin/sh
docker build -t kleed .
docker run -v $(pwd):/home/klee/workspace --rm -it kleed /bin/bash
