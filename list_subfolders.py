import os
import argparse

def list_contents(folder_path, output_file=None, base_url=None, include_files=False):
    paths = []

    for root, dirs, files in os.walk(folder_path):
        if include_files:
            # Add file paths
            for file_name in files:
                relative_path = os.path.relpath(os.path.join(root, file_name), folder_path)
                paths.append(relative_path)

        # Add subfolder paths
        for dir_name in dirs:
            relative_path = os.path.relpath(os.path.join(root, dir_name), folder_path)
            paths.append(relative_path)

    if base_url:
        # Append the base URL and replace backslashes with forward slashes
        paths = [os.path.join(base_url, path).replace("\\", "/") for path in paths]

    if output_file:
        with open(output_file, 'w') as file:
            for path in paths:
                file.write(path + '\n')
    else:
        for path in paths:
            print(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List subfolder and file paths.")
    parser.add_argument("-o", "--output", help="Specify an output file for paths")
    parser.add_argument("-u", "--url", help="Specify a base URL to prepend to paths")
    parser.add_argument("-f", "--files", action="store_true", help="Include file paths")
    parser.add_argument("folder_path", nargs='?', default=os.getcwd(), help="Path to the folder to enumerate")

    args = parser.parse_args()
    folder_path = args.folder_path
    output_file = args.output
    base_url = args.url
    include_files = args.files

    list_contents(folder_path, output_file, base_url, include_files)
