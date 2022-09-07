#!/usr/bin/env python3
#
import requests
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    # ConsoleSpanExporter,
)
from opentelemetry.sdk.resources import Resource
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

provider = TracerProvider(
    resource=Resource.create({"service.name": "shopper"}),
)
# provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
provider.add_span_processor(
    BatchSpanProcessor(
        JaegerExporter(agent_host_name="localhost", agent_port=6831)
    )
)
trace.set_tracer_provider(provider)

RequestsInstrumentor().instrument()
with trace.get_tracer(__name__).start_as_current_span(
    "going to the grocery store"
):
    res = requests.get("http://localhost:5000")
    print(res.text)
