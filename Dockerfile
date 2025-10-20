# Dockerfile - AI Video Upscaler Pro v2.0 (CUDA 12.8 Compatible)
FROM nvidia/cuda:12.3.1-cudnn9-devel-ubuntu22.04

# Evitar prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    CUDA_HOME=/usr/local/cuda \
    PATH=/usr/local/cuda/bin:${PATH} \
    LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH} \
    FORCE_CUDA=1 \
    TORCH_CUDA_ARCH_LIST="6.0;6.1;7.0;7.5;8.0;8.6;8.9;9.0"

# Metadata
LABEL maintainer="AI Video Upscaler Pro" \
      description="Complete AI Video Upscaling: Real-ESRGAN + FILM + RIFE + CodeFormer" \
      version="2.0.0"

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.10 \
    python3-pip \
    python3-dev \
    git \
    wget \
    curl \
    ffmpeg \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libgoogle-perftools-dev \
    build-essential \
    cmake \
    ninja-build \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Actualizar pip
RUN python3 -m pip install --no-cache-dir --upgrade pip setuptools wheel

# Crear directorio de aplicación
WORKDIR /app

# Copiar y instalar dependencias
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copiar scripts de setup
COPY setup.sh start.sh ./
RUN chmod +x setup.sh start.sh

# Crear estructura de directorios
RUN mkdir -p /app/models /app/workspace /app/examples /app/assets /app/repos /app/logs

# Ejecutar setup (clonar repos y descargar modelos)
RUN ./setup.sh

# Copiar código de la aplicación
COPY app/ ./app/
COPY config.yaml .
COPY scripts/ ./scripts/
COPY vsh.py .
RUN chmod +x vsh.py
COPY assets/ ./assets/ 2>/dev/null || true

# Exponer puerto Gradio
EXPOSE 7860

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=120s --retries=3 \
    CMD curl -f http://localhost:7860/ || exit 1

# Variables de entorno por defecto
ENV GRADIO_SERVER_NAME="0.0.0.0" \
    GRADIO_SERVER_PORT="7860" \
    CUDA_VISIBLE_DEVICES="0" \
    NUMEXPR_MAX_THREADS="16"

# Comando de inicio
CMD ["./start.sh"]
