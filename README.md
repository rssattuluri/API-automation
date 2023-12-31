# Python API Automation Framework

Custom hybrid framework to test REST APIs

### Tech stack
Python - 3.12.1
Request - HTTP requests
Pytest - Testing framework
Reporting - Allure report, Pytest HTML
Test data - CSV, Excel, Json
Parallel execution - X distribute

**How to install packages:**
```
pip install requests pytest pytest-html faker allure-pytest jsonschema
```
**To freeze your package version:**
```
pip freeze > requirements.txt
```
**To install the freeze version:**
```
pip install -r requirements.txt

```
```
pip install pytest-xdist
```
```
pytest -n auto tests/integration_test/test_create_booking.py
```

To Work with the Excel
```
pip install openpyxl
```

To work wit JSON Schema
```
pip install jsonschema
```

