ARG BUILD_FROM
FROM $BUILD_FROM

WORKDIR /app

RUN apk --no-cache add gcc musl-dev git sqlite-dev curl jq
RUN mkdir -p /app/core

# Determine the architecture and download the appropriate pre-release binary
RUN arch=$(uname -m) && \
    case "$arch" in \
        x86_64) binary="donetick_Linux_x86_64.tar.gz" ;; \
        aarch64) binary="donetick_Linux_arm64.tar.gz" ;; \
        armv7l) binary="donetick_Linux_armv7.tar.gz" ;; \
        armv6l) binary="donetick_Linux_armv6.tar.gz" ;; \
        *) echo "Unsupported architecture: $arch" && exit 1 ;; \
    esac && \
    latest_prerelease=$(curl --silent "https://api.github.com/repos/donetick/donetick/releases" | \
        jq -r '[.[] | select(.prerelease == true)] | first | .tag_name') && \
    if [[ "${latest_prerelease}" == "null" || -z "${latest_prerelease}" ]]; then \
        echo "No pre-release found, falling back to latest stable release" && \
        latest_prerelease=$(curl --silent "https://api.github.com/repos/donetick/donetick/releases/latest" | jq -r .tag_name); \
    fi && \
    echo "Downloading ${latest_prerelease}" && \
    curl -fL "https://github.com/donetick/donetick/releases/download/${latest_prerelease}/${binary}" | tar -xz -C /app/core

# Copy entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh


# Expose necessary ports
EXPOSE 2021

# Set the entrypoint script
CMD ["/app/entrypoint.sh"]
