from pathlib import Path


def clean_folder(path: Path):
    for file in path.iterdir():
        if file.is_file():
            if file.suffix in [".log", ".zst", ".gz"]:
                file.unlink()

def main():
    for folder in Path(__file__).parent.iterdir():
        if folder.is_dir() and folder.name != ".git":
            clean_folder(folder)

if __name__ == "__main__":
    main()
