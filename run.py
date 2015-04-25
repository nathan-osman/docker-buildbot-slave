#!/usr/bin/env python

from errno import EEXIST
from os import environ, makedirs, path
from subprocess import call


# Base directory for the slave
basedir = '/var/lib/buildbot/slaves/slave'

# Ensure that the slave's info/ directory exists
try:
    makedirs(path.join(basedir, 'info'))
except OSError as e:
    if e.errno != EEXIST:
        raise

# Store the admin's email or use a suitable default if not provided
with open(path.join(basedir, 'info', 'admin'), 'w') as f:
    f.write(environ.get('EMAIL', 'buildbot@localhost'))

# TODO: determine some basic information about the machine
with open(path.join(basedir, 'info', 'host'), 'w') as f:
    f.write('BuildBot Docker Container')

# Run the builder
call([
    '/usr/bin/twistd',
    '--nodaemon',
    '--no_save',
    '-y',
    '/var/lib/buildbot/slaves/slave/buildbot.tac',
])
