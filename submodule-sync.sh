#!/bin/bash

git submodule update --init
cd base-xapp/oai-oran-protolib
git pull
git checkout deliverable_neu