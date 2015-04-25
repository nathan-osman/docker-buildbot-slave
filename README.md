## Docker BuildBot Slave

Docker container providing a 64-bit BuildBot slave.

### Running the Container

A few environment variables are required when launching a container:

- `HOST` - hostname of the BuildBot master
- `NAME` - name for the slave
- `PASSWORD` - password used for authenticating with the master

There are two additional (optional) parameters:

- `PORT` - port to use for connecting to the master
- `EMAIL` - email address displayed in the master web interface

The following example launches a slave instance:

    docker run \
        -d \
        -e HOST=example.org \
        -e NAME=slave01 \
        -e PASSWORD=passw0rd \
        nathanosman/buildbot-slave-amd64
