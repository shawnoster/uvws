#!/bin/bash
set -e

PROJECT_ROOT="$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")"
VIRTUAL_ENV="$PROJECT_ROOT/.venv"

cd "$PROJECT_ROOT" || exit
SERVICE_NAME=$1
if [ ! -d "packages/$SERVICE_NAME" ]; then
  echo "Error: Directory packages/$SERVICE_NAME does not exist."
  exit 1
fi

pushd "packages/$SERVICE_NAME" >/dev/null || exit

printf '%s\n' "Releasing $SERVICE_NAME..."

"$VIRTUAL_ENV/bin/semantic-release" -v version

"$VIRTUAL_ENV/bin/semantic-release" -v publish

popd >/dev/null || exit

