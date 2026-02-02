#!/usr/bin/env bash
# Shared utility functions for Developer-tools scripts

# Fetch a URL with retries and timeout
# Usage: fetch_with_retry URL
# Returns content on stdout; exits 1 on failure after all retries
fetch_with_retry() {
  local url="$1" retries=3 delay=2 attempt
  for attempt in $(seq 1 "$retries"); do
    if result=$(curl --max-time 30 -fsSL "$url" 2>/dev/null); then
      printf '%s' "$result"
      return 0
    fi
    if [ "$attempt" -lt "$retries" ]; then
      echo "Fetch failed (attempt $attempt/$retries), retrying in ${delay}s..." >&2
      sleep "$delay"
      delay=$((delay * 2))
    fi
  done
  echo "Failed to fetch $url after $retries attempts." >&2
  return 1
}

# Clone a git repo with retries and timeout
# Usage: git_clone_with_retry URL TARGET_DIR
git_clone_with_retry() {
  local url="$1" target="$2" retries=3 delay=2 attempt
  for attempt in $(seq 1 "$retries"); do
    rm -rf "$target"
    if GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=30 \
       git clone --depth 1 "$url" "$target" >/dev/null 2>&1; then
      return 0
    fi
    if [ "$attempt" -lt "$retries" ]; then
      echo "Clone failed (attempt $attempt/$retries), retrying in ${delay}s..." >&2
      sleep "$delay"
      delay=$((delay * 2))
    fi
  done
  echo "Failed to clone $url after $retries attempts." >&2
  return 1
}
