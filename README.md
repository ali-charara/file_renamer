# File Renamer

This project allows you to rename the files in the given directory in a sophisticated manner.

To execute the cli, you need to open a terminal command with python and run:

```
python -m file_renamer --deep [folder_path]
```

- `folder_path` is the root path of the directory to process.
- `--deep` if you want to rename all the nested files in the given directory.

You can update the `WHITELIST_EXTENSIONS` to tell the cli which extensions to handle. You can also update the headers of the files to avoid in `PRIVATE_HEADERS`. By default, folder's names are always formatted if not tagged as private folders. Finally, you can also modify `DEV_PROJECT_INDICATORS` which contains the indicators of project folders it must not touch. As long as your projects contains one of the specified indicator, it won't be processed by the renamer.

## TO DO

- improve formatting to `snake_case`:
  - handle dates and special sequences of characters formatting
  - cast letter's variations to base letter (e.g. 'é' --> 'e')
- add other formatters
- add tests to ensure that the formatting and renaming is done properly
- give possibility to restrict renaming to either folders or files or both.
- handle easy execution from any workspace
- remove unwanted patterns if possible:
  - `_\[\d{5}\]` for some downloaded files from mails
  - `_(\d)` for copies
- add NLP formatting feature
