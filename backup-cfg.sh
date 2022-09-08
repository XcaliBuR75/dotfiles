#!/usr/bin/env bash

mkdir -p .config-backup && \
config checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | \
xargs -I{} cp --parents {} .config-backup/

