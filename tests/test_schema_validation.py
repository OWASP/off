import jsonschema
from jsonschema.exceptions import SchemaError, ValidationError
import json

schema_file = "owasp.off.schema.json"

def _load_finding(finding_file):
    finding = ""
    try:
        finding_f = open(finding_file, "r")
        finding = json.load(finding_f)
    except ValueError:
        print("Problem parsing finding file")
    return finding

def _load_json_schema(filename):
    schema_file = open(filename, "r")
    schema = json.load(schema_file)
    return schema

def _validate(finding, schema):
    valid = True
    try:
        v = jsonschema.Draft7Validator(schema)
        for error in sorted(v.iter_errors(finding), key=str):
            print(error.message)
            valid = False

    except SchemaError as e:
        print("There is an error with the schema") 
        valid = False
    except ValidationError as e:
        print(e) 
        print("---------")
        print(e.absolute_path)
        print("---------")
        print(e.absolute_schema_path)
        valid = False
    return valid

def test_example_finding():
    data = _load_finding("example.finding.json")
    schema = _load_json_schema(schema_file)
    result = _validate(data,schema)
    assert result == True, "The schema should validate the example file"

def test_bad_format_finding():
    data = _load_finding("tests/badformat.finding.json")
    schema = _load_json_schema(schema_file)
    result = _validate(data,schema)
    assert result == False, "The schema should not validate the example file"

def test_extra_data_finding():
    data = _load_finding("tests/extradata.finding.json")
    schema = _load_json_schema(schema_file)
    result = _validate(data,schema)
    assert result == False, "The schema should validate the example file"

def test_incomplete_finding():
    data = _load_finding("tests/incomplete.finding.json")
    schema = _load_json_schema(schema_file)
    result = _validate(data,schema)
    assert result == False, "The schema should not validate the example file"
