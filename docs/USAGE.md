# AI Video Upscaler Pro - Usage Guide

## Quick Start

### Web Interface

1. **Start the application**:
   ```bash
   docker-compose up
   ```

2. **Access the web interface**:
   Open your browser and navigate to `http://localhost:7860`

3. **Upload your video**:
   - Drag and drop your video file
   - Or click to browse and select
   - Supported formats: MP4, MOV, AVI, MKV, WEBM, FLV

4. **Choose a preset**:
   - **Quick (2x)**: Fast processing for testing
   - **Balanced (4x)**: Best quality/speed ratio (recommended)
   - **Quality (4x + RIFE)**: Maximum quality with interpolation
   - **Anime (4x + RIFE)**: Optimized for animated content
   - **Cinema (4x + FILM)**: Cinematic smooth motion

5. **Process your video**:
   - Click "PROCESAR VIDEO"
   - Monitor progress in real-time
   - Wait for processing to complete

6. **Download the result**:
   - Click the download button
   - Your enhanced video is ready!

## Advanced Usage

### Command Line Interface

Process a single video:
```bash
python scripts/process_video.py input.mp4 -o output.mp4 -p balanced
```

Batch process multiple videos:
```bash
python scripts/process_video.py video1.mp4 video2.mp4 -o ./output -p quality
```

### Custom Configuration

Edit `config.yaml` to customize:
- Model paths
- Processing settings
- Server configuration
- Preset definitions

## Tips & Best Practices

1. **Start with Quick preset**: Test with Quick preset first to ensure everything works
2. **Short videos first**: Process shorter videos (1-3 min) before long ones
3. **GPU is essential**: CPU processing is extremely slow
4. **Monitor VRAM**: Keep an eye on GPU memory usage
5. **Backup originals**: Always keep your original video files

## Troubleshooting

### GPU Not Detected
```bash
# Check NVIDIA drivers
nvidia-smi

# Verify CUDA
python -c "import torch; print(torch.cuda.is_available())"
```

### Out of Memory
- Reduce tile_size in config.yaml
- Enable half_precision: true
- Process shorter video segments

### Slow Processing
- Verify GPU is being used
- Check CUDA installation
- Use Quick preset for testing

## Examples

See the `examples/` folder for sample videos and expected results.
