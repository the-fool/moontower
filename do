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

docker_build () {
    docker build -t mtc_email .
}

mail_server () {
    docker run -it -p 8080:8080 -e MG_KEY=$MG_KEY mtc_email
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
    docker_build) docker_build;;
    mail_server) mail_server;;
    aws) aws;;
    help|"") usage;;
    *) wrong_command "$cmd";;
esac
