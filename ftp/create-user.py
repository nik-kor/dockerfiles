#!/usr/local/bin/python

import pexpect

child = pexpect.spawn('pure-pw useradd joe -u ftpuser -d /home/ftpusers/joe');

child.expect('Password: ');
child.sendline('123456');

child.expect('Enter it again: ');
child.sendline('123456');

child.expect(pexpect.EOF);

print child.before;
