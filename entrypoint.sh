#!/bin/sh
uvicorn django_with_strawberry_grahpql.asgi:application --host 0.0.0.0 --port 8000 $@