"""AI Video Upscaler Pro - Application Package"""

__version__ = "2.0.0"
__author__ = "AI Video Labs"
__description__ = "Professional AI Video Upscaling with Real-ESRGAN, FILM, RIFE, CodeFormer"

from pathlib import Path

# Define base paths
BASE_DIR = Path(__file__).parent.parent
MODELS_DIR = BASE_DIR / "models"
WORKSPACE_DIR = BASE_DIR / "workspace"
CONFIG_FILE = BASE_DIR / "config.yaml"

__all__ = [
    "__version__",
    "__author__",
    "__description__",
    "BASE_DIR",
    "MODELS_DIR",
    "WORKSPACE_DIR",
    "CONFIG_FILE",
]
