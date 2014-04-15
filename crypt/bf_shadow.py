#!/usr/bin/python
#
# Copyright (C) 2014
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
import crypt
import sys

_ALGORITHM_SHA512 = 6

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print "Ex.: %s -s /etc/shadow -d dict.txt -o output.txt" % sys.argv[0]
        sys.exit(0)

    salt = None
    data = {'user': [], 'pass': []}

    with open(sys.argv[2], 'r') as fd:
        for line in fd.readlines():
            if "$" in line:
                login, algorithm_id, salt, hashed_pwd = line.split("$")
                shadow_pass = "${0}${1}${2}".format(
                    algorithm_id,
                    salt,
                    hashed_pwd.split(":")[0]
                )
                salt_to_crypt_pass = "$%s$%s$" % (algorithm_id, salt)
                if int(algorithm_id) == _ALGORITHM_SHA512:
                    with open(sys.argv[4], 'r') as f_pass:
                        for dict_pass in f_pass.readlines():

                            if dict_pass == "\n":
                                continue

                            encrypt_pass = crypt.crypt(
                                dict_pass.strip("\n"),
                                salt_to_crypt_pass
                            )

                            if encrypt_pass == shadow_pass:
                                print "Found pass! Login %s" % login.strip(":")
                                data['user'].append(login.strip(":"))
                                data['pass'].append(dict_pass.strip("\n"))

    with open(sys.argv[6], 'w+') as fd_write:
        if len(data['user']) > 0:
            for u, p in zip(data['user'], data['pass']):
                fd_write.write("Login: %s Pass: %s\n" % (u, p))
        else:
            fd_write.write("No user/password matched!")
