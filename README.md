# OFF - OWASP Findings Format

The OWASP Findings Format is a standardized structure for security items.

# Why?

The idea behind OFF is to provide a unified *open independent and trusted* format that tools can export.

As this standard format is adopted and used, it will facilitate: 
1. Standardized representation of security findings in dashboards and such
2. Standardized format for mining data out of large sets of findings from different tools

# How to Use It

The OFF project initially defines a JSON Schema for findings.  Simply produce JSON that meets the validation requirements defined in the schema and offer this as an export option.

# Setup for Testing

## Python

Set up the environment in python.

```sh
pipenv --python 3
git clone https://github.com/owasp/off.git
cd off
pipenv install
pipenv shell
pytest
```

See the `tests/test_schema_validation.py` for an example of how to use the schema in python.

## Node.js

Set up the environment in JavaScript.

```
npm install ajv
node simpletest.js
```

### Command Line

We can use AJV to validate from the command line.
```
npm install ajv-cli
ajv validate -s owasp.off.schema.json -d example.finding.json
```
See:  http://epoberezkin.github.io/ajv/#command-line-interface

# Credits

The idea for OFF came from a Dallas OWASP Meeting where a participant indicated that the Indianapolis OWASP
Chapter had conceived of this idea and made many exhortations to advance this as a standard.

# References

The standard:  http://json-schema.org/latest/json-schema-validation.html

Implementations: 
* https://www.npmjs.com/package/json-validation
* https://code.tutsplus.com/tutorials/validating-data-with-json-schema-part-2--cms-25640



