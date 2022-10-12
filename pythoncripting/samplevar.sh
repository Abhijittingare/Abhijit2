#!/bin/bash
SAMPLEVAR="tHIS IS SAMPLE VARIABLE"
function callmethod {
local SAMPLEVAR="VARIABLE INSIDE CALL METHOD"
echo $SAMPLEVAR
}
echo $SAMPLEVAR
callmethod
echo $SAMPLEVAR

