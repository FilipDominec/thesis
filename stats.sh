#!/bin/bash
cat *.tex | wc | sed "s/^/`date  --rfc-3339\=date`/" >> stats.txt
