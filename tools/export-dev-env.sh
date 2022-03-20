#!/usr/bin/env bash

# Run this file as `./tools/export-dev-env.sh` to produce development
# environment with the superset of all the requirements in all the targets.
# This environment is created  in `.venv/devenv`.
#
# You can then point IDE to it or activate using
#   source .venv/devenv/bin/activate
# and all the packages, including tooling (ipython, mypy, pants itself) will be
# available.
#
# PYTHONPATH is also tweaked so that you can run ipython and do
#   from codelearn.<etc>
# and it will recognize your current development setup.

set -eou pipefail

THIS_SCRIPT_DIR="$(realpath "$(dirname "$0")")"
REPO_DIR="$(realpath "${THIS_SCRIPT_DIR}/..")"

if [ ! -d "${REPO_DIR}/.git" ]; then
    echo "${REPO_DIR} is not root of the repo. Maybe path of this script changed?"
    exit 1
fi

VENV=$REPO_DIR/.venv/devenv
PIP="${VENV}/bin/pip"

python3 -m venv --copies "${VENV}"

"${PIP}" install pip --upgrade

"${PIP}" install -r <(./pants dependencies :: |
    xargs ./pants filter --target-type=python_requirement |
    xargs ./pants peek |
jq -r '.[]["requirements"][]')

cd $(${VENV}/bin/python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
echo $REPO_DIR > devenv.pth
