#!/usr/bin/env python

from errno import EEXIST
from os import environ, makedirs, path
from subprocess import call

import psutil


# From http://stackoverflow.com/a/1094933/193619
def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


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

# Determine some basic information about the host
INFO = {
    'CPU Count': psutil.cpu_count(),
    'Memory': sizeof_fmt(psutil.virtual_memory().total),
}

# Display the information
with open(path.join(basedir, 'info', 'host'), 'w') as f:
    f.write('BuildBot Docker Container\n\n')
    for label, value in INFO.items():
        f.write('%-15s%s\n' % (
            '%s:' % label,
            value,
        ))

# Run the builder
call([
    '/usr/bin/twistd',
    '--nodaemon',
    '--no_save',
    '-y',
    '/var/lib/buildbot/slaves/slave/buildbot.tac',
])
