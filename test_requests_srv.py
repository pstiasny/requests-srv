import consul
import requests_srv


def test_getting_getting_a_service():
    c = consul.Consul()
    c.agent.service.register('httpd', port=80)
    response = requests_srv.get('http://_httpd._tcp.service.consul/index.html')
    assert response.status_code == 200
