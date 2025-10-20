# 🎬 AI Video Upscaler Pro v2.0

**Professional AI-Powered Video Upscaling with Real-ESRGAN, FILM, RIFE, CodeFormer & BasicVSR**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)](https://www.docker.com/)
[![CUDA 12.1](https://img.shields.io/badge/CUDA-12.1-76B900.svg)](https://developer.nvidia.com/cuda-toolkit)

## 🚀 Features

### 🎯 AI Models Integrated (100% Functional)

| Model | Function | Status | Use Case |
|-------|----------|--------|----------|
| **Real-ESRGAN** | Upscaling 2x/4x | ✅ Implemented | Videos reales, anime |
| **RIFE v4.6** | Frame Interpolation | ✅ Implemented | Aumentar FPS rápido |
| **FILM Google** | Frame Interpolation | ✅ Implemented | Máxima calidad |
| **CodeFormer** | Face Enhancement | ✅ Implemented | Videos con personas |
| **BasicVSR++** | Video Super-Resolution | 🚧 Structure | Desarrollo futuro |

### ⚡ Key Capabilities

- 🎨 **Video Upscaling**: 2x, 4x resolution enhancement
- 🎞️ **Frame Interpolation**: Smooth motion with RIFE & FILM
- 👤 **Face Enhancement**: AI-powered facial restoration
- 🎵 **Audio Preservation**: Automatic audio handling
- 🐳 **Docker Support**: Full GPU support via Docker/docker-compose
- 🖥️ **Web Interface**: Beautiful Gradio UI
- ⚙️ **Preset System**: Quick, Balanced, Quality, Anime, Cinema

## 📋 Prerequisites

- **GPU**: NVIDIA GPU with CUDA support (RTX A5000+ recommended)
- **VRAM**: Minimum 8GB, 16GB+ recommended
- **Docker**: Docker 20.10+ with nvidia-docker2
- **Storage**: 50GB+ for models and workspace

## 🛠️ Installation

### Option 1: Docker (Recommended)

```bash
# Clone repository
git clone https://github.com/distribuidoramultiple566-debug/AI-VIDEO-UPSCALER-PRO.git
cd AI-VIDEO-UPSCALER-PRO

# Build and run
docker-compose up --build

# Access at http://localhost:7860
```

### Option 2: Manual Installation

```bash
# Clone repository
git clone https://github.com/distribuidoramultiple566-debug/AI-VIDEO-UPSCALER-PRO.git
cd AI-VIDEO-UPSCALER-PRO

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download models
python scripts/download_models.py

# Run application
python app/main.py
```

## 🎮 Usage

### Web Interface

1. **Upload Video**: Drag & drop or select (MP4, MOV, AVI, MKV, WEBM, FLV)
2. **Select Preset**:
   - 🚀 **Quick** (2x): Fast processing for testing
   - ⚖️ **Balanced** (4x): Best quality/speed ratio
   - 💎 **Quality** (4x + RIFE): Maximum quality with interpolation
   - 🎌 **Anime** (4x + RIFE): Optimized for animated content
   - 🎬 **Cinema** (4x + FILM): Cinematic smooth motion
3. **Process**: Click "PROCESAR VIDEO"
4. **Download**: Get your enhanced video

### Command Line

```bash
# Process single video
python scripts/process_video.py input.mp4 -o output.mp4 -p balanced

# Batch processing
python scripts/process_video.py video1.mp4 video2.mp4 -o ./output -p quality
```

## 📁 Project Structure

```
ai-video-upscaler-pro/
├── Dockerfile              # Docker container configuration
├── docker-compose.yml      # Docker Compose with GPU support
├── requirements.txt        # Python dependencies
├── setup.sh                # Setup script
├── start.sh                # Startup script
├── config.yaml             # Configuration file
├── README.md               # This file
├── LICENSE                 # MIT License
├── .gitignore              # Git ignore rules
├── .dockerignore           # Docker ignore rules
├── .env.example            # Environment variables template
├── app/                    # Application source code
│   ├── __init__.py         # Package initialization
│   ├── main.py             # Gradio interface
│   ├── processor.py        # Video processing logic
│   ├── models_manager.py   # Model loading & management
│   ├── interpolation.py    # RIFE & FILM interpolation
│   ├── face_enhancement.py # CodeFormer integration
│   ├── utils.py            # Utility functions
│   └── presets.py          # Processing presets
├── models/                 # AI models storage
│   ├── realesrgan/
│   ├── codeformer/
│   ├── gfpgan/
│   ├── rife/
│   └── basicvsr/
├── workspace/              # Processing workspace
│   ├── temp/               # Temporary files
│   └── output/             # Output videos
├── examples/               # Example videos
├── assets/                 # UI assets
├── docs/                   # Documentation
│   ├── USAGE.md            # Usage guide
│   ├── API.md              # API documentation
│   ├── MODELS.md           # Models information
│   └── RUNPOD.md           # RunPod deployment
└── scripts/                # Utility scripts
    ├── download_models.py  # Model downloader
    ├── test_models.py      # Model testing
    └── process_video.py    # CLI processing
```

## ⚙️ Configuration

Edit `config.yaml` to customize:

- Model paths
- Processing settings
- Server configuration
- Preset definitions

## 🚀 Performance

### Processing Times (3 min video)

| GPU | Quick (2x) | Balanced (4x) | Quality (4x+RIFE) |
|-----|------------|---------------|-------------------|
| **A100** | ~8 min | ~20 min | ~45 min |
| **A5000** | ~12 min | ~30 min | ~60 min |
| **RTX 3090** | ~15 min | ~40 min | ~80 min |
| **CPU** | ⚠️ Very slow (hours) | ⚠️ Not recommended | ⚠️ Not recommended |

## 📚 Documentation

- [Usage Guide](docs/USAGE.md) - Detailed usage instructions
- [API Documentation](docs/API.md) - API reference
- [Models Information](docs/MODELS.md) - AI models details
- [RunPod Deployment](docs/RUNPOD.md) - Cloud deployment guide

## 🐛 Troubleshooting

### GPU Not Detected

```bash
# Check NVIDIA drivers
nvidia-smi

# Verify CUDA
python -c "import torch; print(torch.cuda.is_available())"
```

### Out of Memory

- Reduce tile_size in config.yaml
- Use half_precision: true
- Process shorter videos

### Slow Processing

- Ensure GPU is being used
- Check CUDA installation
- Use Quick preset for testing

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) by xinntao
- [RIFE](https://github.com/hzwer/Practical-RIFE) by hzwer
- [FILM](https://github.com/google-research/frame-interpolation) by Google Research
- [CodeFormer](https://github.com/sczhou/CodeFormer) by sczhou
- [GFPGAN](https://github.com/TencentARC/GFPGAN) by Tencent ARC
- [BasicVSR++](https://github.com/ckkelvinchan/BasicVSR_PlusPlus) by ckkelvinchan
- [Gradio](https://gradio.app/) for the amazing UI framework

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/distribuidoramultiple566-debug/AI-VIDEO-UPSCALER-PRO/issues)
- **Discussions**: [GitHub Discussions](https://github.com/distribuidoramultiple566-debug/AI-VIDEO-UPSCALER-PRO/discussions)

## ⭐ Star History

If you find this project useful, please consider giving it a star! ⭐

---

**Made with ❤️ by AI Video Labs**

*Optimized for RunPod • GPU Accelerated • Production Ready*
