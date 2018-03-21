FROM joit/flask-env-docker:0.0.1

WORKDIR /root/sweext_web

COPY ./ ./

ENV RUN_IN_PROD=True

    # setup sweext
RUN pip3 install sweext.tar.gz \
    && pip3 install -e . \
    #setup gunicorn
    && mv sweext_supervisord.conf /etc/supervisor/conf.d \
    && mkdir -p /var/log/supervisor \
       /opt/supervisor \
       /root/sweext_web/sweext_web/logger/debug_logs /root/sweext_web/sweext_web/logger/error_logs \
    && touch /opt/supervisor/sweext_web.log \
    && rm sweext.tar.gz

EXPOSE 5000

CMD ["/usr/bin/supervisord"]
