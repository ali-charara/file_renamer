from argparse import ArgumentParser, Namespace
import os
import logging

from .constants import WHITELIST_EXTENSIONS, FORMATTER, LOGGER_VERBOSE
from .path_processing import search_files_and_directories, rename_file
from .utils import input_yes_no_answer

logging.basicConfig()
logger = logging.getLogger("file renamer")
logger.setLevel(LOGGER_VERBOSE)


def parse_arguments() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("folder_path", help="the root path of the considered folder")
    parser.add_argument(
        "--deep",
        "-d",
        action="store_true",
        default=False,
        help="whether to look for nested children of the root folder (default: False)",
    )

    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_arguments()
    number_formatted_files = 0
    if input_yes_no_answer(
        f"do you want to process {os.path.abspath(arguments.folder_path)}?"
    ):
        logger.info("Processing files...")
        candidates = search_files_and_directories(arguments.folder_path, arguments.deep)
        for file_path, is_directory in reversed(candidates):
            if is_directory or (
                not is_directory
                and os.path.splitext(file_path)[1][1:] in WHITELIST_EXTENSIONS
            ):
                full_path, dot_extension = os.path.splitext(file_path)
                file_name = full_path.split(os.sep)[-1]
                if file_name != (formatted_name := FORMATTER(file_name)):
                    rename_file(file_path, f"{formatted_name}{dot_extension}")
                    logger.info((f"{file_name} → {formatted_name}"))
                    number_formatted_files += 1

        print(f"Number of files formatted: {number_formatted_files}")
