from pathlib import Path
import shutil
import json

EXTENSION_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv", ".odf"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Video": [".mp4", ".mov", ".mkv", ".avi"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code": [".py", ".cpp", ".js", ".html", ".css", ".json", ".sql", ".sh", ".java", ".c"],
    "Executables": [".exe", ".msi", ".dmg", ".pkg", ".deb"]
}

logfilename = ".OrganizedFile_log.json"

def get_unique_name(dest_folder, file):
    target_path = dest_folder/file.name
    counter = 1

    while target_path.exists():
        new_name = f"{file.name}_{counter}{file.suffix}"
        target_path = dest_folder/new_name
        counter += 1
    return target_path

def define_catagory(file: Path):
    #stem = file.stem
    ext = file.suffix
    dest_catagory = "Others"
    for catagory, extension in EXTENSION_CATEGORIES.items():
        if ext in extension:
            dest_catagory = catagory
            break
    return dest_catagory

def record_and_move(item: Path, destination: Path, history: list, maindir: Path, dry_run=True):
    if dry_run:
        print(f"[DRY RUN] {item.name} --▶ {destination}")
    else :
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(item), str(destination))
        print(f"[MOVED] {item.name} --▶ {destination}")

        history.append({
            "original": str(item.resolve()),
            "current": str(destination.resolve())
        })
        save_transaction_log(maindir, history)


def undo_transaction(target_dir: Path):
    log_path = target_dir/logfilename

    if not log_path.exists():
        print(f"[!] The Transaction log '{logfilename}' Does Not Exist...")
        return
    with open(log_path, "r", encoding="utf-8")as f:
        history = json.load(f)

    if not history:
        print(f"[!] Trasnsaction log is empty...")
        log_path.unlink()
        return

    print(f"Reverting {len(history)} file moves...\n")
    count = 0

    for entry in reversed(history):
        current_path = Path(entry["current"])
        original_path = Path(entry["original"])

        if current_path.exists():
            original_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(current_path), str(original_path))
            print(f" • Restored: {current_path.name} --▶ {original_path.parent.name}")
            count += 1
        else:
            print(f" • [Skiped] File missing: {current_path.name}")

    log_path.unlink()
    print(f"\n[✓] Sucessfully reverted {count} files. History cleared...")

def save_transaction_log(target_dir: Path, history: list):
    log_path = target_dir/logfilename
    try:
        with open(log_path, "w", encoding="utf-8")as f:
            json.dump(history, f, indent=4)
        print(f"[✓] Transaction log saved to {logfilename}")
    except FileNotFoundError:
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4)
            print(f"[!] File Not Found...\nCreating a new File in {log_path}")

    except json.JSONDecodeError:
        print(f"[!] File Not Found...\nCreating a new File in {log_path}")
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4)
            print(f"[!] {logfilename} was empty or corrupted. Re-initalisating that file..")

def cleanup_empty_folder(target_dir: Path, category: dict):
    category.update({"Others":[]})
    count = 0
    for cat in category.keys():
        folder = target_dir/cat
        if folder.exists() and folder.is_dir():
            try:
                folder.rmdir()
                print(f" • Removed empty directory: {cat}/")
                count = 1
            except OSError:
                pass
    if count == 0 :
        print(f"[!] Found nothing to delete..")
    category.pop("Others")

def main():

    print("==================================================")
    print("            DESKTOP FILE ORGANISER                ")
    print("==================================================")

    dir_name = input("Target Directory:  ")
    dir = Path.home()/dir_name

    if not dir.is_dir() or not dir.exists():
        print(f"[!] The File Directory '{dir}' does not exixted or not a File Directory..")
        exit(0)

    print("[?] Run Mode: ")
    print(" 1. Dry Run (Preview moves without touching the files): ")
    print(" 2. Live Run(Move Files): ")
    mode = input("Select Mode (1/2):  ")

    hist = []

    if mode == "1":
        for item in dir.iterdir():
            if item.is_dir() or item.name.startswith("."):
                continue
            elif item.resolve() == Path(__file__).resolve():
                continue
            else:
                catagory = define_catagory(item)
                dest_folder = dir/catagory
                name = get_unique_name(dest_folder, item)
                destination_path = dest_folder/name
                record_and_move(item, destination_path, hist, dir, True)

        ch = input("Do you want to reverse any previous organisation process (Y/N):  ")
        if ch.lower() == "y":
            undo_transaction(dir)
        else :
            chh = input("Do you want to clean up the empty folder(Y/N):  ")
            if chh.lower() == "y":
                cleanup_empty_folder(dir, EXTENSION_CATEGORIES)
            else:
                print("\nThank You :)\n")
                exit(0)

    elif mode == "2":
        try:
            for item in dir.iterdir():
                if item.is_dir() or item.name.startswith("."):
                    continue
                elif item.resolve() == Path(__file__).resolve():
                    continue
                else:
                    catagory = define_catagory(item)
                    dest_folder = dir/catagory
                    name = get_unique_name(dest_folder, item)
                    destination_path = dest_folder/name
                    record_and_move(item, destination_path, hist, dir, False)

            ch = input("Do you want to reverse the Process (Y/N):  ")
            if ch.lower() == "y":
                undo_transaction(dir)
            else :
                chh = input("Do you want to clean up the empty folder(Y/N):  ")
                if chh.lower() == "y":
                    cleanup_empty_folder(dir, EXTENSION_CATEGORIES)
                else:
                    print("\nThank You :)\n")
                    exit(0)

        except Exception as e:
            print(f"[!] Error Ocuured: {e}.")
            undo_transaction(dir)
    else:
        print("[!] Invalid choise...")

if __name__ == "__main__":
    main()
