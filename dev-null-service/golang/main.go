//
// main.go
// Copyright (C) 2019 Shlomi Fish <shlomif@cpan.org>
//
// Distributed under terms of the MIT license.
//

package main

import (
	"devnull"
	"log"
	"net"
	"net/http"
)

type emptyHandler struct{}

func (e emptyHandler) ServeHTTP(r http.ResponseWriter, req *http.Request) {
}

func main() {
	l, err := net.Listen("tcp", ":9000")
	if err != nil {
		log.Fatal(err)
	}

	devnull.Serve(l, emptyHandler{})
}
