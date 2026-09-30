from pathlib import Path


def get_asset(file_name: str) -> str:
    """Return the absolute path to a resource file."""
    assets_folder = Path(__file__).resolve().parent
    return str(assets_folder / file_name)
