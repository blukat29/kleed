FROM klee/klee

ENV KLEE_LIB="/home/klee/klee_build/klee/Release+Asserts/lib/"
ENV LD_LIBRARY_PATH="$KLEE_LIB:$LD_LIBRARY_PATH"
ENV PATH="/home/klee/bin:$PATH"

RUN mkdir -p /home/klee/bin

RUN echo "klee" | sudo --stdin apt-get -y install python2.7
RUN ln -s $KLEE_LIB/libkleeRuntest.so $KLEE_LIB/libkleeRuntest.so.1.0

ADD solve.py /home/klee/bin/solve.py
ADD ktest.py /home/klee/bin/ktest.py

VOLUME /home/klee/workspace

