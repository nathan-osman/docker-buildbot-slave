#!/bin/bash
# Build an armhf Docker image of Ubuntu 14.04 (Trusty Tahr)
# Copyright 2015 - Nathan Osman

set -e

ARCH="armhf"
SUITE="trusty"
CHROOT="/var/chroot/${SUITE}-${ARCH}"
MIRROR="http://ports.ubuntu.com"
IMAGE="nathanosman/ubuntu-armhf"

# Ensure the script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root"
    exit 1
fi

# Invoke the script
DEBOOTSTRAP=qemu-debootstrap ./mkimage.sh \
    -d "${CHROOT}" \
    -t "${IMAGE}" \
    debootstrap \
    --arch="${ARCH}" \
    --components=main,universe \
    "${SUITE}" \
    "${MIRROR}"

# Push the newly built image
docker push "${IMAGE}"
