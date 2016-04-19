#!/bin/bash

for file in unstructured/*; 
do  
  python restruct_v4.py $file > $file.out.txt;
