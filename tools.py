# Modules
import json
from custom_logger import *
from pathlib import Path
import os

def read_json():
    log_info("Reading JSON...")

    filename: Path = Path("StorableSidebar.json")
    if os.name == "nt": # Windows
        arc_root_parent_path: Path = Path(
            os.path.expanduser(r"~\AppData\Local\Packages")
        )
        arc_root_paths: list[Path] = [
            f
            for f in arc_root_parent_path.glob("*")
            if f.name.startswith("TheBrowserCompany.Arc")
        ]
        if len(arc_root_paths) != 1:
            raise FileNotFoundError

        library_path: Path = Path(
            arc_root_paths[0].joinpath(r"LocalCache\Local\Arc")
        ).joinpath(filename)

    else:
        library_path: Path = Path(
            os.path.expanduser("~/Library/Application Support/Arc/")
        ).joinpath(filename)

    data: dict = {}

    if filename.exists():
        with filename.open("r", encoding="utf-8") as f:
            log_debug(f"Found {filename} in current directory.")
            data = json.load(f)

    elif library_path.exists():
        with library_path.open("r", encoding="utf-8") as f:
            log_debug(f"Found {filename} in Library directory.")
            data = json.load(f)

    else:
        log_error(
            '> File not found. Look for the "StorableSidebar.json" '
            '  file within the "~/Library/Application Support/Arc/" folder.'
        )
        raise FileNotFoundError

    return data
