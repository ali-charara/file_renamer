import os

from .constants import PRIVATE_HEADERS


def search_files_and_directories(
    root_folder_path: str, deep: bool = False
) -> list[tuple[str, bool]]:
    assert os.path.isdir(root_folder_path)

    paths = []
    for file_name in os.listdir(root_folder_path):
        file_path = os.path.join(root_folder_path, file_name)
        if file_name[0] not in PRIVATE_HEADERS:
            paths.append((file_path, os.path.isdir(file_path)))
            if deep and os.path.isdir(file_path):
                paths.extend(search_files_and_directories(file_path, deep))

    return paths


def rename_file(file_path: str, new_file_name: str) -> None:
    os.rename(file_path, f"{os.path.dirname(file_path)}/{new_file_name}")
