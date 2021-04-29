#!/bin/bash
#Eddies script to launch Discord bot

pkill chatthing.py

nohup python3.7 chatthing.py >/dev/null 2>&1 &
