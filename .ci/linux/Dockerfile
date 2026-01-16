# Thomas Chromium - Linux Build Environment
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    clang \
    lld \
    git \
    python3 \
    python3-pip \
    curl \
    wget \
    pkg-config \
    ninja-build \
    libglib2.0-dev \
    libgtk-3-dev \
    libxss-dev \
    libnss3-dev \
    libatk1.0-dev \
    libatk-bridge2.0-dev \
    libdrm-dev \
    libxkbcommon-dev \
    libpango1.0-dev \
    libcairo2-dev \
    libasound2-dev \
    libpulse-dev \
    libcups2-dev \
    libxrandr-dev \
    libgbm-dev \
    && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /build

# Default command
CMD ["/bin/bash"]
