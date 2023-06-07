#!/bin/bash

git submodule update --init
git submodule update --remote --merge
cd base-xapp/oai-oran-protolib
git pull
git checkout deliverable_neu
