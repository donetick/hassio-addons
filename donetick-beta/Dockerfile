ARG BUILD_FROM
FROM $BUILD_FROM

WORKDIR /app

RUN apk --no-cache add gcc musl-dev git sqlite-dev curl
RUN mkdir -p /app/core

# Use the pre-release version maintained in config.yaml by the release-sync workflow.
RUN --mount=type=bind,source=config.yaml,target=/tmp/donetick-addon-config.yaml \
    arch=$(uname -m) && \
    case "$arch" in \
        x86_64) binary="donetick_Linux_x86_64.tar.gz" ;; \
        aarch64) binary="donetick_Linux_arm64.tar.gz" ;; \
        armv7l) binary="donetick_Linux_armv7.tar.gz" ;; \
        armv6l) binary="donetick_Linux_armv6.tar.gz" ;; \
        *) echo "Unsupported architecture: $arch" && exit 1 ;; \
    esac && \
    version=$(awk '/^version:/ { gsub(/["\047\r]/, "", $2); print $2; exit }' /tmp/donetick-addon-config.yaml) && \
    case "$version" in \
        ''|[!0-9]*|*[!0-9A-Za-z.+-]*) echo "Invalid add-on version in config.yaml: $version" >&2; exit 1 ;; \
    esac && \
    echo "Downloading v${version}" && \
    curl -fL --retry 3 -o /tmp/donetick.tar.gz \
        "https://github.com/donetick/donetick/releases/download/v${version}/${binary}" && \
    tar -xzf /tmp/donetick.tar.gz -C /app/core && \
    rm /tmp/donetick.tar.gz

# Copy entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh


# Expose necessary ports
EXPOSE 2021

# Set the entrypoint script
CMD ["/app/entrypoint.sh"]
