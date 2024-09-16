# Django with Strawberry GraphQL

This project demonstrates the integration of Django with Strawberry GraphQL.

## Features

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Strawberry GraphQL**: A new GraphQL library for Python, designed to be simple to use and extend.

## Requirements

- Python 3.12+
- Django 5.1+
- Strawberry GraphQL

## Development

- To start the whole stack, run:

  ```
  $ make up
  ```

- To take down the stack, run:

  ```
  $ make down
  ```

- To view logs for a specific service, use `logs-{service}`. You can also customize the number of log lines to display with the `log_lines` argument:

  ```
  $ make logs-api log_lines=50
  ```