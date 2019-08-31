#! /bin/sh
#
# run_server.sh
# Copyright (C) 2019 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under terms of the MIT license.
#
set -e -x
export GOPATH="$GOPATH:$PWD"
go run main.go
