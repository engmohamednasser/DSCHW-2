From python:3.8

ADD test.py .


RUN pip install --upgrade pip && \
    pip install numpy && \
    pip install cython numpy scipy pandas

CMD ["python" ,"./test.py"]
