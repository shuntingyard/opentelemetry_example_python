# My OpenTelemetry example for Python

## Python instrumentation inspired by
https://words.boten.ca/Practical-OpenTelemetry-part-1-Python/

### Installing Jaeger back-end for code example
At the time of repo creation (and provided you have a working docker installation)
the simplest way to set up a local back-end for Jaeger tracing is

<pre>
docker run -d --name jaeger \
  -e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \
  -e COLLECTOR_OTLP_ENABLED=true \
  -p 6831:6831/udp \
  -p 6832:6832/udp \
  -p 5778:5778 \
  -p 16686:16686 \
  -p 4317:4317 \
  -p 4318:4318 \
  -p 14250:14250 \
  -p 14268:14268 \
  -p 14269:14269 \
  -p 9411:9411 \
  jaegertracing/all-in-one:1.37
</pre>

Source https://www.jaegertracing.io/docs/1.37/getting-started/

## Goals
See how application monitoring can be integrated via back-ends (Jaeger, Prometheus)
or even generate alerts (e.g. Prometheus <-> Nagios, Prometheus <-> Checkmk).
