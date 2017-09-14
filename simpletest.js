// This is an example script that validates different OWASP OFF Finding JSON examples.
//
// See https://github.com/OWASP/off for additional detail.
// 

// Set up a validator
var Ajv = require('ajv');
var ajv = new Ajv();
var schema = require('./owasp.off.schema.json')
var validate = ajv.compile(schema)

// Test a good case (happy path)
var data = require('./example.finding.json')
var valid = validate(data);
if (valid) {
  console.log('User data is valid');
} else {
  console.log('User data is INVALID!');
  console.log(ajv.errorsText());
}

// // ---  THESE ARE NOT WORKING!

// Test bad format
var data1 = require('./tests/badformat.finding.json')
var valid = validate(data1);
if (valid) {
 	console.log('Warning:  User data is valid but should be invalid.');
} else {
	console.log('Correctly identified invalid format.')
}

// Test incomplete
var data1 = require('./tests/incomplete.finding.json')
var valid = validate(data1);
if (valid) {
 	console.log('Warning:  User data is valid but should be incomplete.');
} else {
	console.log('Correctly identified imcomplete finding.')
}

// Test extra
var data2 = require('./tests/extradata.finding.json')
var valid = validate(data2);
if (valid) {
 	console.log('Warning:  User data is valid but should be invalid with extra fields.');
} else {
	console.log('Correctly identified extra data in finding.')
}
