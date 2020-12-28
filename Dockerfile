FROM python:3-buster
RUN pip install flywheel-sdk
RUN rm -rf /var/cache/apk/*

ENV FLYWHEEL=/flywheel/v0

RUN mkdir -p ${FLYWHEEL}
COPY run.py ${FLYWHEEL}/run.py

ENTRYPOINT ["python run.py"]
