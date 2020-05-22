import pytest
from main import find_files


def test_find_files():
    suffix = ".c"
    path = "./testdir"
    file_paths = (
        # Windows
        ['./testdir\\subdir1\\a.c',
         './testdir\\subdir3\\subsubdir1\\b.c',
         './testdir\\subdir5\\a.c',
         './testdir\\t1.c'],
        # Linux
        ['./testdir/subdir1/a.c',
         './testdir/subdir3/subsubdir1/b.c',
         './testdir/subdir5/a.c',
         './testdir/t1.c']
    )
    assert sorted(find_files(suffix, path)) in file_paths

    suffix = ".gitkeep"
    path = "./testdir"
    file_paths = (
        ['./testdir\\subdir2\\.gitkeep', './testdir\\subdir4\\.gitkeep'],
        ['./testdir/subdir2/.gitkeep', './testdir/subdir4/.gitkeep']
    )
    assert sorted(find_files(suffix, path)) in file_paths

    suffix = ".csv"
    path = "./testdir"
    assert len(find_files(suffix, path)) == 0

    suffix = ".c"
    path = "./testdir/subdir5"
    file_paths = (
        ['./testdir/subdir5\\a.c'],
        ['./testdir/subdir5/a.c']
    )
    assert find_files(suffix, path) in file_paths

    suffix = ".c"
    path = "./crazydir"
    with pytest.raises(IOError, match="No such directory .*"):
        find_files(suffix, path)


if __name__ == '__main__':
    pytest.main()
