# requests_srv

A simple wrapper/plugin for [requests](docs.python-requests.org) for
[RFC-2782](https://tools.ietf.org/html/rfc2782)
style services, i.e. for FQDNs starting with an underscore it will 
access a resource pointed by an SRV record instead of the A record.
Useful for seamless service discovery with DNS-based service discovery
service like [Consul](https://consul.io/).

## Use as a drop-in replacement for requests

```python
import requests_srv as requests
print requests.get('http://_consul._http.service.consul/v1/catalog/services').text
```

## Use with your custom session

```python
from requests_srv import SRVResolverHTTPAdapter

session = Session()
session.mount('http://_', SRVResolverHTTPAdapter())
session.mount('https://_', SRVResolverHTTPAdapter())
```

## Run tests

Test environent is set up in docker containers.  To set up and run:

```sh
bash test.sh
```
