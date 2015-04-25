## Docker BuildBot Slave

Docker container providing a 64-bit BuildBot slave.

### Running the Container

A few environment variables are required when launching a container:

- `HOST` - hostname of the BuildBot master
- `NAME` - name of the slave
- `PASSWORD` - password used for authenticating with the master

There are two additional (optional) variables:

- `PORT` - port to use for connecting to the master
- `EMAIL` - email address displayed in the master web interface

The following example launches a slave instance:

    docker run \
        -d \
        -e HOST=example.org \
        -e NAME=slave01 \
        -e PASSWORD=passw0rd \
        nathanosman/buildbot-slave-amd64

### Adding Packages

The container only provides the packages necessary to run the BuildBot slave
and the `build-essential` Ubuntu package. If your project requires additional
packages for building, simply create a new container based on this one and
install the packages from there.

For example, to install the Qt 5 libraries:

    FROM nathanosman/buildbot-slave-amd64

    RUN \
        apt-get update && \
        apt-get install -y qtbase5-dev && \
        rm -rf /var/lib/apt/lists/*

You can then launch the container as described above.
