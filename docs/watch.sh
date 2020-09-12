#!/bin/bash

watchmedo shell-command --patterns="*.py;*.rst" --recursive --command="poetry run make clean; poetry run make html" ..
