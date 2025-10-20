#!/usr/bin/env python3
"""Script to download all AI models for Video Upscaler Pro"""

import sys
import requests
from pathlib import Path
from tqdm import tqdm
import hashlib
from loguru import logger

# Model configuration
MODELS_CONFIG = {
    "realesrgan": {
        "x4plus": {
            "url": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth",
            "filename": "RealESRGAN_x4plus.pth",
            "size_mb": 64
        },
        "x2plus": {
            "url": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth",
            "filename": "RealESRGAN_x2plus.pth",
            "size_mb": 64
        },
        "anime": {
            "url": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth",
            "filename": "RealESRGAN_x4plus_anime_6B.pth",
            "size_mb": 18
        }
    },
    "codeformer": {
        "main": {
            "url": "https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/codeformer.pth",
            "filename": "codeformer.pth",
            "size_mb": 360
        },
        "detection": {
            "url": "https://github.com/xinntao/facexlib/releases/download/v0.1.0/detection_Resnet50_Final.pth",
            "filename": "detection_Resnet50_Final.pth",
            "size_mb": 105
        },
        "parsing": {
            "url": "https://github.com/xinntao/facexlib/releases/download/v0.2.2/parsing_parsenet.pth",
            "filename": "parsing_parsenet.pth",
            "size_mb": 82
        }
    },
    "gfpgan": {
        "v1.3": {
            "url": "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth",
            "filename": "GFPGANv1.3.pth",
            "size_mb": 332
        },
        "v1.4": {
            "url": "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth",
            "filename": "GFPGANv1.4.pth",
            "size_mb": 348
        }
    },
    "rife": {
        "v4.6": {
            "url": "https://github.com/hzwer/Practical-RIFE/releases/download/4.6/flownet.pkl",
            "filename": "flownet.pkl",
            "size_mb": 51
        }
    }
}

def download_file(url, output_path, desc="Downloading"):
    """Download a file with progress bar"""
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        
        with open(output_path, 'wb') as f, tqdm(
            desc=desc,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                size = f.write(chunk)
                pbar.update(size)
        return True
    except Exception as e:
        logger.error(f"Error downloading {url}: {e}")
        return False

def verify_file(filepath, expected_size_mb):
    """Verify downloaded file"""
    if not filepath.exists():
        return False
    
    size_mb = filepath.stat().st_size / (1024 * 1024)
    # Allow 5% variance
    if abs(size_mb - expected_size_mb) / expected_size_mb > 0.05:
        logger.warning(f"{filepath.name}: Size mismatch (got {size_mb:.1f}MB, expected {expected_size_mb}MB)")
        return False
    return True

def download_all_models(models_dir: Path = Path("./models"), force: bool = False):
    """Download all models"""
    logger.info("="*80)
    logger.info("AI Video Upscaler Pro - Model Downloader")
    logger.info("="*80)
    
    total_downloaded = 0
    total_skipped = 0
    total_failed = 0
    total_size_mb = 0
    
    for category, models in MODELS_CONFIG.items():
        logger.info(f"Category: {category.upper()}")
        category_dir = models_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)
        
        for model_name, model_info in models.items():
            output_path = category_dir / model_info["filename"]
            
            # Check if already exists
            if output_path.exists() and not force:
                if verify_file(output_path, model_info["size_mb"]):
                    logger.info(f"✓ {model_info['filename']} already exists")
                    total_skipped += 1
                    continue
                else:
                    logger.warning(f"{model_info['filename']} exists but corrupted, re-downloading...")
                    output_path.unlink()
            
            # Download
            logger.info(f"Downloading {model_info['filename']} ({model_info['size_mb']} MB)...")
            success = download_file(
                url=model_info["url"],
                output_path=output_path,
                desc=f"{model_name}"
            )
            
            if success and verify_file(output_path, model_info["size_mb"]):
                logger.info(f"✓ {model_info['filename']} downloaded successfully")
                total_downloaded += 1
                total_size_mb += model_info["size_mb"]
            else:
                logger.error(f"✗ Failed to download {model_info['filename']}")
                total_failed += 1
    
    # Summary
    logger.info("="*80)
    logger.info("DOWNLOAD SUMMARY")
    logger.info("="*80)
    logger.info(f"Downloaded: {total_downloaded} models ({total_size_mb:.1f} MB)")
    logger.info(f"Skipped: {total_skipped} models (already exist)")
    logger.info(f"Failed: {total_failed} models")
    logger.info("="*80)
    
    if total_failed > 0:
        logger.warning("Some models failed to download. Please check your internet connection and try again.")
        return False
    
    logger.info("✓ All models downloaded successfully!")
    return True

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Download AI models for Video Upscaler Pro")
    parser.add_argument("--models-dir", type=str, default="./models", help="Models directory")
    parser.add_argument("--force", action="store_true", help="Force re-download existing models")
    
    args = parser.parse_args()
    models_dir = Path(args.models_dir)
    
    success = download_all_models(models_dir, force=args.force)
    sys.exit(0 if success else 1)
