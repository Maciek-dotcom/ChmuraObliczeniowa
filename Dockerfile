FROM python:3.8.2-alpine
ARG TCP_PORT_ARG=3338
ENV TCP_PORT_ENV=${TCP_PORT_ARG}
WORKDIR /server/
ADD server.py /server/
RUN touch logs
RUN touch index.html
CMD pip install pytz; python server.py -ptcp ${TCP_PORT_ENV}
EXPOSE ${TCP_PORT_ARG}/tcp