#!/bin/sh

set -eux

cd "$(dirname "$0")"

data_URL="http://sato-data.s3.amazonaws.com"

curl -Lo tmp.zip "$data_URL/tmp.zip" > tmp.zip
curl -Lo sherlock/pretrained.zip "$data_URL/pretrained.zip"
curl -Lo sato/topic_model/LDA_cache.zip "$data_URL/LDA_cache.zip"
