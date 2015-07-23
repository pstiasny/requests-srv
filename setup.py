# encoding: utf8

import setuptools

setuptools.setup(
    name="requests_srv",
    version="0.0.1",
    py_modules=["requests_srv"],
    author=u"Paweł Stiasny",
    author_email="pawelstiasny@gmail.com",
    url="http://github.com/pstiasny/requests-srv",
    license="Apache 2.0",
    description="A wrapper for Requests supporting DNS SRV records.",
    keywords=['requests'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'requests',
        'dnspython',
        'pytest',
        'python-consul',
    ],
)
