#!/bin/sh
sudo docker build -t kleed .
sudo docker run -v $(pwd):/home/klee/workspace --rm -it kleed /bin/bash
