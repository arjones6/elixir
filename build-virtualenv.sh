#!/bin/bash

set -e
set -x

cd $(dirname "${BASH_SOURCE[0]}")

# try to find pg_config path
if [ -z "$(which pg_config)" ]; then
    PGDIR="$(ls -d /usr/pgsql-* | tail -n1)"
    if [ -n "$PGDIR" ] && [ -d "$PGDIR/bin" ]; then
        export PATH="$PGDIR/bin:$PATH"
    fi
fi

# set up clean virtualenv
TARGET="virtualenv-$(date +%Y%m%d-%H%M%S)"
rm -rf $TARGET
PYTHON=${PYTHON:-"python"}
virtualenv --python=$PYTHON $TARGET
source $TARGET/bin/activate

# upgrade to latest pip
pip install --upgrade pip

# install tools
pip install "nose"
pip install "ipython"

# install requirements
pip install -r requirements.txt

# switch symlink
rm -rf virtualenv
ln -s $TARGET virtualenv
