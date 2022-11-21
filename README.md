# File Renamer

This project allows you to rename the files in the given directory in a sophisticated manner.

To execute the cli, you need to open a terminal command with python and run:

```bash
python -m file_renamer --deep [folder_path]
```

- `folder_path` is the root path of the directory to process.
- `--deep` if you want to rename all the nested files in the given directory.
- `--ascii` if you want to cast the file_names to ascii format.
- `--clean` if you want to remove identified noisy patterns such as " copy", " (1)", etc.

You may add `.renamer_ignore` in the subfolders you would like to avoid processing. If the formatting attempt matches an existing file, the file won't be processed.

You can update the `WHITELIST_EXTENSIONS` to tell the cli which extensions to handle. You can also update the headers of the files to avoid in `PRIVATE_HEADERS`. By default, folder's names are always formatted if not tagged as private folders. You can also modify `PROJECT_INDICATORS` which contains the indicators of project folders it must not touch. As long as your projects contains one of the specified indicator, it won't be processed by the renamer. Finally, to specify new unwanted patterns to be processed automatically by the cleaner, you may modify `UNWANTED_PATTERNS`.

## TO DO

- improve formatting to `snake_case`:
  - handle dates and special sequences of characters formatting
- add other formatters
- add arguments folder_paths_to_ignore for the execution
- add tests to ensure that the formatting and renaming is done properly
- give possibility to restrict renaming to either folders or files or both.
- handle easy execution from any workspace
- explore NLP formatting feature
- expections formats:
  - `LYONStage IAEthiqueMMM01012022`
  - `Cours (livre + notes de cours)`
  - `MVA-VCdimNeuralNetworks → mva_vc_neural_networks`
  