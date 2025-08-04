#!/bin/bash

echo "Running API tests with HTML report..."

# Activate virtual environment (optional - uncomment if needed)
# source .venv/bin/activate

pytest tests/ --html=report.html --self-contained-html -v

echo "Tests completed. Report generated: report.html"
