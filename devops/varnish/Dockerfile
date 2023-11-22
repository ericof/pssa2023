# syntax=docker/dockerfile:1
FROM varnish:7.4

LABEL maintainer="Érico Andrei <ericof@plone.org>" \
      org.label-schema.name="pssa2023-varnish" \
      org.label-schema.description="Plone Symposium South America 2023 Varnish image." \
      org.label-schema.vendor="Érico Andrei"

COPY etc/varnish.vcl /etc/varnish/default.vcl
