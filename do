#! /bin/bash

set -e

cmd=$1

serve() {
    hugo server
}

build() {
    hugo
}

usage() {
    echo './do serve'
}

case $cmd in
    serve) serve;;
    build) build;;
    help|"") usage;;
    *) wrong_command "$cmd";;
esac
