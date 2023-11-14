OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c[5];

h q[0];
h q[1];
h q[2];
p(5 * pi / 4) q[0];
p(5 * pi / 2) q[1];
p(5 * pi) q[2];
swap q[0], q[2];
h q[0];
cu1(-pi / 2) q[0], q[1];
h q[1];
cu1(-pi / 2) q[1], q[2];
cu1(-pi / 4) q[0], q[2];
h q[2];

// @columns [0,0,0,1,1,1,2,3,5,6,7,8,9]