#!/usr/bin/python
#
# Copyright (C) 2015
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
import socket
import os
import ssl
import sys


def main():
    pem_file = "/etc/pki/ovirt-engine/ca.pem"

    if not os.path.exists(pem_file):
        print("You must specify a valid pem file")
        return -1

    ssl_sock = ssl.wrap_socket(socket.socket(socket.AF_INET,
                                             socket.SOCK_STREAM),
                               ca_certs=pem_file,
                               cert_reqs=ssl.CERT_REQUIRED)

    try:
        ssl_sock.connect(('engine.localdomain', 443))
        cert = (ssl_sock.getpeercert())
    except Exception:
        raise
    finally:
        ssl_sock.close()

    pem_issuer = "Issuer: \n" \
        "\t Country Name: {cn} \n" \
        "\t Organization Name: {on} \n" \
        "\t Common Name: {cmn} \n".format(cn=cert['issuer'][0][0][1],
                                          on=cert['issuer'][1][0][1],
                                          cmn=cert['issuer'][2][0][1])

    pem_validity = "Validity: \n" \
        "\t Not Before: {nb} \n" \
        "\t Not After: {na} \n".format(nb=cert['notBefore'],
                                       na=cert['notAfter'])
    pem_subject = "Subject: \n" \
        "\t Country Name: {cn} \n" \
        "\t Organization Name: {on} \n" \
        "\t Common Name: {cmn} \n".format(cn=cert['subject'][0][0][1],
                                          on=cert['subject'][1][0][1],
                                          cmn=cert['subject'][2][0][1])

    print(pem_issuer)
    print(pem_validity)
    print(pem_subject)
    print("Version: {0}".format(cert['version']))
    print("Serial Number: {0}".format(cert['serialNumber']))

    return 0

if __name__ == '__main__':
    sys.exit(main())
