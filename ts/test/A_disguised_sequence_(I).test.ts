/// <reference path="../typings/globals/mocha/index.d.ts" />
/// <reference path="../typings/globals/chai/index.d.ts" />

import solution = require('../src/A_disguised_sequence_(I)');
import {assert} from "chai";

function testing(n, expected) {
  assert.equal(solution.G964.fcn(n), expected)
}
describe("Fixed Tests fcn", function(){
  it("Basic tests", function() {
    testing(17, 131072);
    testing(21, 2097152);
    testing(14, 16384);
    testing(43, 8796093022208);
    testing(19, 524288);
  });
});
