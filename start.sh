#!/bin/bash
# Start script for AI Video Upscaler Pro

set -e

echo "========================================"
echo "AI Video Upscaler Pro v2.0"
echo "========================================"

# Check GPU
if command -v nvidia-smi &> /dev/null; then
    echo "GPU Information:"
    nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv,noheader
    echo "========================================"
else
    echo "WARNING: No GPU detected. Processing will be slow."
    echo "========================================"
fi

# Start the application
echo "Starting Gradio interface..."
echo "Access at: http://localhost:7860"
echo "========================================"

python3 /app/app/main.py
