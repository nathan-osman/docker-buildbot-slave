from os import environ, path

from buildslave.bot import BuildSlave
from twisted.application import service
from twisted.python.logfile import LogFile
from twisted.python.log import ILogObserver, FileLogObserver


# Get the directory of this file
basedir = path.abspath(path.dirname(__file__))

# Create the application
application = service.Application('buildslave')

# Create a log file for the application
logfile = LogFile.fromFullPath(path.join(basedir, 'twistd.log'))
application.setComponent(ILogObserver, FileLogObserver(logfile).emit)

# Parameters (such as the host, slave name, & password) are expected to be
# provided as environment variables - assume that the required ones are present
BuildSlave(
    environ.get('HOST'),
    environ.get('PORT', 9989),
    environ.get('NAME'),
    environ.get('PASSWORD'),
    basedir,
    600,
    0,
).setServiceParent(application)
