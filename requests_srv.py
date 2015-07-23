from urlparse import urlparse, urlunparse

import dns.resolver
from requests import Session, HTTPError
from requests.adapters import HTTPAdapter, DEFAULT_POOLSIZE, DEFAULT_RETRIES, DEFAULT_POOLBLOCK


class SRVResolverHTTPAdapter(HTTPAdapter):
    def __init__(self, dns_hosts=None, dns_port=None, **kwargs):
        self.dns_hosts = dns_hosts
        self.dns_port = dns_port
        self.resolver = dns.resolver.Resolver()
        if dns_hosts is not None:
            self.resolver.nameservers = dns_hosts
        if dns_port is not None:
            self.resolver.port = dns_port
        super(SRVResolverHTTPAdapter, self).__init__(**kwargs)

    def get_connection(self, url, proxies=None):
        parsed = urlparse(url)
        host, port = self.__resolve(parsed.netloc)
        redirected_url = urlunparse((
            parsed.scheme,
            '%s:%d' % (host, port), 
            parsed.path,
            parsed.params,
            parsed.query,
            parsed.fragment
        ))
        return super(SRVResolverHTTPAdapter, self).get_connection(redirected_url, proxies=proxies)

    def __resolve(self, service):
        answers = self.resolver.query(service, 'SRV')
        return answers[0].target, answers[0].port

session = Session()
session.mount('http://_', SRVResolverHTTPAdapter())
session.mount('https://_', SRVResolverHTTPAdapter())

request = session.request
head = session.head
get = session.get
post = session.post
put = session.put
patch = session.patch
delete = session.delete


if __name__ == '__main__':
    from sys import argv
    response = get(argv[1])
    print response.text
