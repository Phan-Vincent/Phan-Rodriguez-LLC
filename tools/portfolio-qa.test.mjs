import assert from 'node:assert/strict';
import {catalogTargets, layoutFailure, motionFailure, footerFailure} from './portfolio-qa.mjs';
// A control can fit the document yet escape its narrower header.
assert.equal(layoutFailure({left: 18, right: 300, viewport: 305, client: 282, scroll: 282, parentLeft: 18, parentRight: 287}), true);
assert.equal(layoutFailure({left: 18, right: 287, viewport: 305, client: 269, scroll: 302}), true);
assert.equal(layoutFailure({left: 18, right: 287, viewport: 305, client: 269, scroll: 269}), false);
// RAF-driven carousel motion has no Web Animations entry.
assert.equal(motionFailure([{animations: 0, positions: [0]}, {animations: 0, positions: [12]}]), true);
assert.equal(motionFailure([{animations: 1, positions: []}]), true);
assert.equal(motionFailure([{animations: 0, positions: [50]}, {animations: 0, positions: [50]}]), false);
assert.equal(footerFailure({top: 700, bottom: 820}, {top: 788, bottom: 844}, 844), true);
assert.equal(footerFailure({top: 600, bottom: 780}, {top: 788, bottom: 844}, 844), false);
assert.deepEqual(catalogTargets('<a href="mockups/el-rey/"></a><a href="./mockups/el-rey/index.html"></a>'), ['mockups/el-rey/index.html']);
assert.throws(() => catalogTargets('<a href="mockups/../private/index.html">bad</a>'));
console.log('QA predicate regression checks passed');
