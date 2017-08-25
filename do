#! /bin/bash

set -e

cmd=$1

serve() {
  hugo server
}

usage() {
    echo './do serve'
}
case $cmd in
    serve) serve;;
    help|"") usage;;
    *) wrong_command "$cmd";;
esac
