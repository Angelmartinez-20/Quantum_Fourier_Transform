OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c[5];

x q[0];
x q[2];
h q[2];
cu1(pi / 2) q[2], q[1];
cu1(pi / 4) q[2], q[0];
h q[1];
cu1(pi / 2) q[1], q[0];
h q[0];
swap q[0], q[2];

// @columns [0,0,1,3,4,5,6,7,8]
