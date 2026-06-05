from pathlib import Path

def find_duplicate_songs(directory_path: str, suffix: str = ".mp3"):
    path_obj = Path(directory_path)
    if not path_obj.exists() or not path_obj.is_dir():
        print("Указанный каталог не существует или не является папкой!")
        return
    files_by_name = {}
    for child in path_obj.rglob(f"*{suffix}"):
        if child.is_file():
            name = child.name
            if name not in files_by_name:
                files_by_name[name] = []
            files_by_name[name].append(child.resolve())
    has_duplicates = False
    print(f"\n--- Результаты поиска дубликатов ({suffix}) ---")
    for name, paths in files_by_name.items():
        if len(paths) > 1:
            has_duplicates = True
            print(f"\nНайден дубликат: {name} (встречается {len(paths)} раз):")
            for p in paths:
                print(f"  -> {p}")
    if not has_duplicates:
        print("Дубликаты не обнаружены.")
