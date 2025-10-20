#!/bin/bash
# Setup script - Download models and clone repositories

set -e

echo "========================================"
echo "AI Video Upscaler Pro - Setup"
echo "========================================"

# Clone repositories if they don't exist
REPOS_DIR="/app/repos"
mkdir -p $REPOS_DIR

echo "Cloning repositories..."

# Real-ESRGAN
if [ ! -d "$REPOS_DIR/Real-ESRGAN" ]; then
    echo "Cloning Real-ESRGAN..."
    git clone https://github.com/xinntao/Real-ESRGAN.git $REPOS_DIR/Real-ESRGAN
fi

# RIFE
if [ ! -d "$REPOS_DIR/RIFE" ]; then
    echo "Cloning RIFE..."
    git clone https://github.com/hzwer/Practical-RIFE.git $REPOS_DIR/RIFE
fi

# CodeFormer
if [ ! -d "$REPOS_DIR/CodeFormer" ]; then
    echo "Cloning CodeFormer..."
    git clone https://github.com/sczhou/CodeFormer.git $REPOS_DIR/CodeFormer
fi

# GFPGAN
if [ ! -d "$REPOS_DIR/GFPGAN" ]; then
    echo "Cloning GFPGAN..."
    git clone https://github.com/TencentARC/GFPGAN.git $REPOS_DIR/GFPGAN
fi

echo "Repositories cloned successfully!"

# Download models using Python script
if [ -f "/app/scripts/download_models.py" ]; then
    echo "Downloading AI models..."
    python3 /app/scripts/download_models.py --models-dir /app/models
else
    echo "Warning: download_models.py not found, skipping model download"
fi

echo "========================================"
echo "Setup completed successfully!"
echo "========================================"
