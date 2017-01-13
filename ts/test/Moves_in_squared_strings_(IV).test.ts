/// <reference path="../typings/globals/mocha/index.d.ts" />
/// <reference path="../typings/globals/chai/index.d.ts" />

import solution = require('../src/Moves_in_squared_strings_(IV)');
import {assert} from "chai";

function testing(actual, expected) {
  assert.equal(actual, expected);
}

describe("Fixed Tests", function() {
    it("Basic tests rot90Counter", function() {
        testing(solution.G964.oper(solution.G964.rot90Counter, "EcGcXJ\naaygcA\nNgIshN\nyOrCZE\neBEqpm\nNkxCgw"),
            "JANEmw\nXchZpg\ncgsCqC\nGyIrEx\ncagOBk\nEaNyeN");
    });
});
describe("Fixed Tests", function() {
    it("Basic tests diag2Sym", function() {        
        testing(solution.G964.oper(solution.G964.diag2Sym, "LmvLyg\nDKELBm\nylJhui\nXRXqHD\nzlisCT\nhPqxYb"),
            "bTDimg\nYCHuBy\nxsqhLL\nqiXJEv\nPlRlKm\nhzXyDL");
    });
});
describe("Fixed Tests", function() {
    it("Basic tests selfieDiag2Counterclock", function() {        
        testing(solution.G964.oper(solution.G964.selfieDiag2Counterclock, "NJVGhr\nMObsvw\ntPhCtl\nsoEnhi\nrtQRLK\nzjliWg"),
            "NJVGhr|gKilwr|rwliKg\nMObsvw|WLhtvh|hvthLW\ntPhCtl|iRnCsG|GsCnRi\nsoEnhi|lQEhbV|VbhEQl\nrtQRLK|jtoPOJ|JOPotj\nzjliWg|zrstMN|NMtsrz");
    });
});
