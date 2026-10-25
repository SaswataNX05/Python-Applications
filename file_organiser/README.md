# Desktop File Organiser (`FILE_ORGANISER.py`)

A lightweight, automated Python CLI tool designed to declutter directories by organizing files into categorized subfolders based on file extensions. It includes safety features such as dry-run previews, conflict-free file renaming, transaction logging, and complete undo/rollback capabilities.

---

## 🚀 Features

- **Automatic Categorization**: Groups files into dedicated folders (`Images`, `Documents`, `Audio`, `Video`, `Archives`, `Code`, `Executables`, and `Others`).
- **Dry Run Mode**: Preview exactly which files will be moved and where without touching anything on your disk.
- **Live Run Mode**: Safely moves files into organized directories and logs every operation.
- **Transaction Logging & Undo System**: Tracks movements in `.OrganizedFile_log.json` to allow rolling back files to their original locations at any time or automatically upon an error.
- **Conflict Resolution**: Generates unique filenames to avoid overwriting existing files in destination folders.
- **Empty Folder Cleanup**: Option to clean up and remove empty category folders after organizing or reverting.
- **Zero Third-Party Dependencies**: Built purely with Python standard libraries (`pathlib`, `shutil`, `json`).

---

## 📁 Supported Categories & Extensions

| Category | File Extensions |
| :--- | :--- |
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg` |
| **Documents** | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`, `.csv`, `.odf` |
| **Audio** | `.mp3`, `.wav`, `.aac`, `.flac` |
| **Video** | `.mp4`, `.mov`, `.mkv`, `.avi` |
| **Archives** | `.zip`, `.tar`, `.gz`, `.rar`, `.7z` |
| **Code** | `.py`, `.cpp`, `.js`, `.html`, `.css`, `.json`, `.sql`, `.sh`, `.java`, `.c` |
| **Executables** | `.exe`, `.msi`, `.dmg`, `.pkg`, `.deb` |
| **Others** | Any file extension not explicitly matched above |

*Note: Hidden files (starting with `.`), directories, and the script itself are automatically skipped.*

---

## 🛠️ Requirements

- **Python 3.6+**
- Standard Python libraries (no `pip install` required):
  - `pathlib`
  - `shutil`
  - `json`

---

## 📖 How to Use

### 1. Run the Script
Open your terminal in the script directory and run:

```bash
python3 FILE_ORGANISER.py
```

### 2. Enter Target Directory
Enter the directory name relative to your user home directory (`~` / `Path.home()`):

```text
Target Directory:  Downloads
```
*(For example, entering `Downloads` targets `/home/<user>/Downloads` or `C:\Users\<user>\Downloads`.)*

### 3. Select Run Mode
You will be prompted to choose an execution mode:

```text
[?] Run Mode: 
 1. Dry Run (Preview moves without touching the files)
 2. Live Run (Move Files)
Select Mode (1/2):
```

- **Option `1` (Dry Run)**: Prints simulated file movements (e.g., `[DRY RUN] file.pdf --▶ /home/.../Documents/file.pdf`) without moving files.
- **Option `2` (Live Run)**: Creates required folders, moves files, prints `[MOVED]` confirmations, and records entries into `.OrganizedFile_log.json`.

### 4. Post-Execution Options
After the run finishes:
- **Undo Option**: Prompt asks if you would like to undo file organization. If confirmed, all moved files are restored to their previous paths.
- **Folder Cleanup Option**: If you choose not to revert, you can opt to delete empty category directories.

---

## 🔄 Reverting / Undo Mechanism

When files are moved in **Live Run** mode:
1. Each move is tracked in a transaction log file named `.OrganizedFile_log.json` inside the target directory.
2. If an error occurs midway through organizing, the script automatically triggers rollback.
3. You can also trigger an undo directly at the prompt.
4. When reverted, each file is moved back to its exact original path, and the transaction log is safely cleared.

---

## ⚙️ Key Functions Overview

- `define_catagory(file)`: Evaluates file extension against predefined categories.
- `get_unique_name(dest_folder, file)`: Generates non-colliding names if a file already exists in destination.
- `record_and_move(...)`: Handles dry-run printing or file transfer and logs movement.
- `undo_transaction(target_dir)`: Reads `.OrganizedFile_log.json`, reverses moves, and removes the log.
- `cleanup_empty_folder(target_dir, category)`: Scans for and removes unoccupied category directories.
