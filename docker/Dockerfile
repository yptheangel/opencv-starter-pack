FROM nvcr.io/nvidia/l4t-pytorch:r32.4.2-pth1.5-py3

RUN rm -f /usr/bin/python && ln -s /usr/bin/python3 /usr/bin/python

RUN apt-get update; apt-get install gcc g++ make-y

RUN python3.6-dev python3-pip

# copy files current from current directory to directory in docker image
COPY /.test.py /test.py

RUN apt-get install onboard -y

RUN apt-get install python3-opencv -y

RUN apt-get install python3-pyqt5 python3-pyqt5.qtwebengine -y
RUN pip3 install qimage2ndarray