#!/usr/bin/env python3
#
import requests
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.sdk.resources import Resource

exporter = ConsoleSpanExporter()
resource = Resource.create({"service.name": "shopper"})
provider = TracerProvider(resource=resource)
span_processor = BatchSpanProcessor(exporter)
provider.add_span_processor(span_processor)
trace.set_tracer_provider(provider)

with trace.get_tracer(__name__).start_as_current_span(
    "going to the grocery store"
):
    res = requests.get("http://localhost:5000")
    print(res.text)
