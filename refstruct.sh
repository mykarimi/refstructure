#!/bin/bash

for file in unstructured/*; 
do  
  python refstruct_v4.py $file > $file.out.txt;
