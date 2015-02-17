#!/bin/bash
cat appendices.tex expe.tex conclusion.tex intro.tex  result.tex theory.tex  | wc | sed "s/^/`date  --rfc-3339\=date`/" >> stats.txt
