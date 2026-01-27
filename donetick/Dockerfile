ARG BUILD_FROM

# ---- Build stage: compile backend and frontend from source ----
FROM golang:1.24-alpine AS builder

RUN apk --no-cache add gcc musl-dev git sqlite-dev curl nodejs npm

# Build frontend
RUN git clone https://github.com/RamiAwar/frontend.git /frontend
WORKDIR /frontend
RUN npm install && npm run build-selfhosted

# Build backend
RUN git clone https://github.com/RamiAwar/donetick.git /build
WORKDIR /build
RUN cp -r /frontend/dist /build/frontend/dist
RUN CGO_ENABLED=1 go build -o /app/core/donetick .

# ---- Runtime stage: Home Assistant base image ----
FROM $BUILD_FROM

WORKDIR /app

RUN apk --no-cache add sqlite-libs
RUN mkdir -p /app/core

COPY --from=builder /app/core/donetick /app/core/donetick
RUN chmod +x /app/core/donetick

# Copy entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose necessary ports
EXPOSE 2021

# Set the entrypoint script
CMD ["/app/entrypoint.sh"]
