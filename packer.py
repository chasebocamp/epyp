import os
import subprocess
import sys
import shutil
from typing import List

# --- PS2 Environment Configuration ---
PS2_GCC = shutil.which("ps2-gcc")
PS2_LD = shutil.which("ps2-ld")
PS2_OBJCOPY = shutil.which("ps2-objcopy")
PS2_EE_MAKER = shutil.which("ee-maker")
# ------------------------------------

REQUIRED_TOOLS = {
    "ps2-gcc": PS2_GCC,
    "ps2-ld": PS2_LD,
    "ps2-objcopy": PS2_OBJCOPY,
    "ee-maker": PS2_EE_MAKER,
}


def abort(msg: str, code: int = 1):
    print(f"Fatal: {msg}")
    sys.exit(code)


def validate_tools():
    missing = [name for name, path in REQUIRED_TOOLS.items() if path is None]
    if missing:
        abort(f"Missing required tools: {', '.join(missing)}")


def run(cmd: List[str], step: str):
    """Run a subprocess with consistent error handling."""
    try:
        subprocess.run(
