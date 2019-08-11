# Some (hopefully) scalable HTTP/HTTPS /dev/null services

Work-in-progress. This was inspired by [a conversation](https://www.shlomifish.org/humour/fortunes/show.cgi?id=mongodb-vs-dev-null) where
a party noted that he belives the setup of https://devnull-as-a-service.com/
is not scalable.

Currently there is an incomplete Golang implementation which was
forked-and-modified from [fcgi.go](https://golang.org/pkg/net/http/fcgi/)
(thanks!) which may or may not work or perform well.

# See Also

* [/dev/null is WebScale links](http://shlomifishswiki.branchable.com/slash-dev-null_is_WebScale/)
