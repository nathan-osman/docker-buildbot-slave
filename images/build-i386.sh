#!/bin/bash
# Build an i386 Docker image of Ubuntu 14.04 (Trusty Tahr)
# Copyright 2015 - Nathan Osman

set -e

ARCH="i386"
SUITE="trusty"
CHROOT="/var/chroot/${SUITE}-${ARCH}"
MIRROR="http://archive.ubuntu.com/ubuntu"
IMAGE="nathanosman/ubuntu-i386"

# Ensure the script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root"
    exit 1
fi

# Invoke the script
./mkimage.sh \
    -d "${CHROOT}" \
    -t "${IMAGE}" \
    debootstrap \
    --arch="${ARCH}" \
    --components=main,universe \
    "${SUITE}" \
    "${MIRROR}"

# Push the newly built image
docker push "${IMAGE}"
