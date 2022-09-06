#!/usr/bin/env python3
#
from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.sdk.resources import Resource

exporter = ConsoleSpanExporter()
resource = Resource.create({"service.name": "grocery_store"})
provider = TracerProvider(resource=resource)
span_processor = BatchSpanProcessor(exporter)
provider.add_span_processor(span_processor)
trace.set_tracer_provider(provider)
app = Flask(__name__)


@app.route("/")
def welcome():
    with trace.get_tracer(__name__).start_as_current_span("welcome message"):
        return "Welcome to the grocery store!"


if __name__ == "__main__":
    app.run()
