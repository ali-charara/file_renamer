import logging
import os
from argparse import ArgumentParser, Namespace
from functools import partial

from unidecode import unidecode

from .constants import (
    FORMATTER,
    LOGGER_VERBOSE,
    REGEX_UNWANTED_PATTERNS,
    WHITELIST_EXTENSIONS,
)
from .path_processing import rename_file, search_files_and_directories
from .utils import input_yes_no_answer, remove_unwanted_patterns

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
    parser.add_argument(
        "--ascii",
        "-a",
        action="store_true",
        default=False,
        help="whether to cast file_names to ascii format (default: False)",
    )
    parser.add_argument(
        "--clean",
        "-c",
        action="store_true",
        default=False,
        help="whether to remove unwanted patterns if possible (e.g. '- copy') (default: False)",
    )

    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_arguments()
    number_formatted_files = 0
    if input_yes_no_answer(
        f"Do you want to process {(absolute_folder_path := os.path.abspath(arguments.folder_path))}?"
    ):
        preprocesser = unidecode if arguments.ascii else lambda x: x
        cleaner = (
            partial(
                remove_unwanted_patterns,
                regex_unwanted_patterns=REGEX_UNWANTED_PATTERNS,
            )
            if arguments.clean
            else lambda x: x
        )

        logger.info("Processing files...")
        # ? relative paths may raise errors due to MAX_PATH limitations on windows for instance
        candidates = search_files_and_directories(absolute_folder_path, arguments.deep)
        for file_path, is_directory in reversed(candidates):
            full_path, dot_extension = os.path.splitext(file_path)
            file_name = full_path.split(os.sep)[-1]
            if (
                is_directory or dot_extension[1:] in WHITELIST_EXTENSIONS
            ) and file_name != (
                formatted_name := FORMATTER(cleaner(preprocesser(file_name)))
            ):
                try:
                    rename_file(
                        file_path,
                        f"{(formatted_name)}{dot_extension}",
                    )
                except FileExistsError:
                    rename_file(
                        file_path,
                        f"{(formatted_name := FORMATTER(preprocesser(file_name)))}{dot_extension}",
                    )

                logger.info(f"{file_name} → {formatted_name}")
                number_formatted_files += 1

        print(f"Number of files formatted: {number_formatted_files}")
