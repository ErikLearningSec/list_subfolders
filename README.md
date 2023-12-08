# Folder Contents List Script

## Overview

This Python script, `list_contents.py`, provides a convenient way to enumerate and list the subfolders and file paths within a specified directory. The script utilizes the `os` and `argparse` modules for file system traversal and command-line argument parsing, respectively. 

## Features

- Lists subfolder paths by default.
- Optionally includes file paths with the `-f` or `--files` flag.
- Supports specifying an output file for saving the paths with the `-o` or `--output` option.
- Allows prepending a base URL to paths using the `-u` or `--url` option.

## Use Case

### Purpose

This tool was developed to streamline tasks I've encountered in day-to-day white box penetration testing. In scenarios where you have access to the source code of a website, the script becomes a valuable asset for identifying potential misconfigurations.

### How it Works

By running this script on your source code directory, you can generate a comprehensive list of subfolders and optionally include file paths. The output can then be piped into an HTTP probing tool like `httpx` to identify paths that may be misconfigured, such as those with directory listing enabled.

### Security Testing Scenarios

- **Website Misconfigurations:** Detect misconfigured websites by identifying exposed paths, which can lead to potential security vulnerabilities.
  
- **File Inclusion Vulnerabilities:** Combine with a File Inclusion Vulnerability to list the source code from a website using an open-source framework/CMS. Clone the source code of that framework/CMS, run the script with the source code, and analyze for potential security risks.

## Usage

### Basic Usage

```bash
python list_contents.py [folder_path]
```
- `folder_path`: Path to the folder to enumerate. Defaults to the current working directory if not provided.

## Options

- `-o, --output`: Specify an output file for saving paths.
- `-u, --url`: Specify a base URL to prepend to paths.
- `-f, --files`: Include file paths in the listing.

## Example

```bash
python list_contents.py /path/to/directory -o paths.txt -u https://example.com -f
```
This command lists subfolder and file paths in `/path/to/directory`, appends `https://example.com` to each path, and saves the result to `paths.txt`.

## Contributions
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
