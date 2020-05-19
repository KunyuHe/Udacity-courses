import argparse
import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.isdir(path):
        raise IOError(f"No such directory {path}.")

    res = []
    files = os.listdir(path)

    for sub_name in files:
        sub_path = os.path.join(path, sub_name)

        if os.path.isfile(sub_path) and sub_path.endswith(suffix):
            res.append(sub_path)

        elif os.path.isdir(sub_path):
            res += find_files(suffix, sub_path)

    return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--suffix', dest='suffix', type=str, default='.c',
                        help="Suffix of the file names to be found")
    parser.add_argument('--path', dest='path', type=str, default='./testdir',
                        help="Path to the top of the file system.")
    args = parser.parse_args()

    #print("\n".join(find_files(args.suffix, args.path)))
    print(f"Files with suffix {args.suffix} under directory {args.path}:")
    print(find_files(args.suffix, args.path))
