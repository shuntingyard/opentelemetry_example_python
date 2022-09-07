#!/usr/bin/env python3
#
from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    # ConsoleSpanExporter,
)
from opentelemetry.sdk.resources import Resource
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

provider = TracerProvider(
    resource=Resource.create({"service.name": "grocery-store"}),
)
# provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
provider.add_span_processor(
    BatchSpanProcessor(
        JaegerExporter(
            agent_host_name="localhost",
            agent_port=6831,
        )
    )
)
trace.set_tracer_provider(provider)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)


@app.route("/")
def welcome():
    with trace.get_tracer(__name__).start_as_current_span("welcome message"):
        return "Welcome to the grocery store!"


if __name__ == "__main__":
    app.run()
