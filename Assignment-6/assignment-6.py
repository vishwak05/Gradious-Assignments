# Finding the Disk Space Usage of Sub Folders in Current Directory

# Using os and argparse library for command line arguments
import os
import argparse

def human_readable_size(size):
    # Function to convert sizes into human readable format
    for unit in ['B','K','M','G','T','P','E','Z']:
        if abs(size) < 1024.0:
            return "%3.1f%s" % (size, unit)
        
        size /= 1024.0
    return "%.1f%s" % (size, 'Y')

def get_dir_size(path, max_depth, current_depth, results, human_readable, rel_path):
    # Getting the size of folders using recurvise method
    # Sums the file sizes in folder and returns folder size
    total = 0
    # Calculating the size of sub folders
    try:
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_symlink():
                    continue  # skip symlinks for safety

                if entry.is_file():
                    # Sum the size of files
                    total += entry.stat(follow_symlinks=False).st_size
                
                elif entry.is_dir():
                    # Getting into folder to sum the file size using recursion
                    sub_rel_path = os.path.join(rel_path, entry.name)

                    if max_depth is None or current_depth < max_depth:
                        subdir_size = get_dir_size(
                            entry.path, max_depth, current_depth+1, results, human_readable, sub_rel_path
                        )
                        # Aggregating folder sizes
                        total += subdir_size
    except PermissionError:
        pass  # skip folders/files you can't access

    # Adding the sizes if within depth limit
    if max_depth is None or current_depth <= max_depth:
        display_size = human_readable_size(total) if human_readable else str(total)
        results.append((display_size, rel_path))
    return total

def main():
    # Adding command line arguments like "-h --max-depth=1"
    parser = argparse.ArgumentParser(description="du - estimate file space usage", add_help=False)

    # Getting the current working directory
    parser.add_argument("directory", nargs="?", default=".", help="Directory to scan")

    # Argument to get the Maximum Depth to calculate the sizes
    parser.add_argument("--max-depth", type=int, help="Maximum depth to display")

    # Argument to print the folder sizes in Human Readable format
    parser.add_argument("-h", "--human-readable", action="store_true", help="Print sizes in human readable format (e.g., 1K 234M 2G)")

    # Additional help argument to understand the arguments
    parser.add_argument("--help", action="help", help="Show this help message and exit")
    args = parser.parse_args()

    directory = os.path.abspath(args.directory)
    results = []

    get_dir_size(
        directory,
        args.max_depth,
        0,
        results,
        args.human_readable,
        '.'
    )

    # Sort to match du output (subdirs before parent)
    results.sort(key=lambda x: x[1].count(os.sep))
    for size, rel_path in results:
        print(f"{size} {rel_path}")

if __name__ == "__main__":
    main()
