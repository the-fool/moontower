#! /bin/bash

set -e

cmd=$1

serve() {
    hugo server
}

build() {
    hugo
    ./node_modules/gulp/bin/gulp.js build
}
aws() {
    aws s3 cp ./public s3://moontowercider.com --recursive
}

usage() {
    echo './do serve'
}

case $cmd in
    serve) serve;;
    build) build;;
    aws) aws;;
    help|"") usage;;
    *) wrong_command "$cmd";;
esac
