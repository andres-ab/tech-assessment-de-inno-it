
# Assessment técnico DE - CSV to JSON Converter

Author: Andrés Armesto

## Overview

This Python package provides a simple tool to convert CSV data into a structured JSON format, suitable for representing average ticket data for different markets.

## Usage

To execute the sample test, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/andres-ab/tech-assessment-de-inno-it.git
    ```

2. Navigate to the `csv-to-json` directory:

    ```bash
    cd csv-to-json
    ```

3. Install the required packages using the provided requirements.txt file:

    ```bash
    python3 -m pip install -r requirements.txt
    ```

4. Run the sample test:

    ```bash
    python3 main.py ../data/raw/MarketAvrgTicketSample.csv ../data/clean/MarketAvrgTicketSample_output_example.json
    ```

This command will convert the provided CSV file (`MarketAvrgTicketSample.csv`) to JSON and save the result in the specified output file (`MarketAvrgTicketSample_output_example.json`).

## Requirements

- Python 3.11
- Dependencies listed in `requirements.txt`

## Docker

Feel free to use the docker-compose YAML to access notebooks. Run `docker compose up` and then browse to `http://localhost:8888/lab`.
