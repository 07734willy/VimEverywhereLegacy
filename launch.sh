#!/usr/bin/env bash

vim -c "py3 import sys;sys.path.append('$(pwd)')" -c "py3 import process; process.run()"
