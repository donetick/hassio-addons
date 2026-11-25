#!/usr/bin/env bash
# Build and run a local dev copy of an app in the devcontainer.
#
# The published apps use uppercase slugs (e.g. "Donetick"),
# and pull a prebuilt image from ghcr.io.
# Building locally makes Supervisor tag the image with the slug,
# and Docker rejects uppercase image names.
# So this copies <folder>/ to <folder>-dev/ (gitignored),
# lowercases the slug and appends "_dev",
# and drops the image: key so Supervisor builds from the Dockerfile.
# The real app folders are never modified.
#
# Usage: .vscode/dev-app.sh <folder> <sync|install|start|rebuild|uninstall>
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
folder="${1:?usage: dev-app.sh <folder> <sync|install|start|rebuild|uninstall>}"
action="${2:?usage: dev-app.sh <folder> <sync|install|start|rebuild|uninstall>}"

src="${repo_root}/${folder}"
dst="${repo_root}/${folder}-dev"
src_config="${src}/config.yaml"

if [[ ! -f "${src_config}" ]]; then
  echo "error: ${src_config} not found" >&2
  exit 1
fi

# Read the slug from the source config,
# stripping optional quotes.
src_slug="$(sed -n -E 's/^slug:[[:space:]]*["'\'']?([^"'\''[:space:]]+)["'\'']?[[:space:]]*$/\1/p' "${src_config}")"
if [[ -z "${src_slug}" ]]; then
  echo "error: could not read slug from ${src_config}" >&2
  exit 1
fi
dev_slug="$(tr '[:upper:]' '[:lower:]' <<<"${src_slug}")_dev"
app="local_${dev_slug}"

sync() {
  echo "Syncing ${folder}/ -> ${folder}-dev/ (slug: ${dev_slug})"
  rsync -a --delete "${src}/" "${dst}/"

  local dst_config="${dst}/config.yaml"
  sed -i -E \
    -e "s/^slug:.*/slug: ${dev_slug}/" \
    -e 's/^name:[[:space:]]*"?([^"]*)"?[[:space:]]*$/name: "\1 (dev)"/' \
    -e '/^#?[[:space:]]*image:/d' \
    "${dst_config}"

  # Fail loudly if the rewrite didn't take,
  # rather than installing something unexpected.
  if ! grep -qx "slug: ${dev_slug}" "${dst_config}"; then
    echo "error: failed to rewrite slug in ${dst_config}" >&2
    exit 1
  fi
  if grep -qE '^[[:space:]]*image:' "${dst_config}"; then
    echo "error: image: key still present in ${dst_config}" >&2
    exit 1
  fi

  ha store reload
}

# Rebuild refuses when the version changed;
# Supervisor wants an update in that case.
rebuild_or_update() {
  local info version latest
  info="$(ha apps info "${app}" --raw-json)"
  version="$(jq -r '.data.version' <<<"${info}")"
  latest="$(jq -r '.data.version_latest' <<<"${info}")"
  if [[ "${version}" != "${latest}" ]]; then
    echo "Version changed (${version} -> ${latest}), updating"
    ha apps update "${app}"
  else
    ha apps rebuild --force "${app}"
  fi
}

case "${action}" in
  sync)
    sync
    ;;
  install)
    sync
    ha apps install "${app}"
    ;;
  start)
    ha apps stop "${app}" || true
    ha apps start "${app}"
    ha apps logs -f "${app}"
    ;;
  rebuild)
    sync
    ha apps stop "${app}" || true
    rebuild_or_update
    ha apps start "${app}"
    ha apps logs -f "${app}"
    ;;
  uninstall)
    ha apps uninstall "${app}"
    ;;
  *)
    echo "error: unknown action '${action}'" >&2
    exit 1
    ;;
esac
