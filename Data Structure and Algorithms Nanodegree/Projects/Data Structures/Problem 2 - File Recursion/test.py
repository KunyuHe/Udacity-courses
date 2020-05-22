import pytest
from main import find_files

TEST_NORMAL = [
    {
        'suffix': ".c",
        'path': "./testdir",
        'file_paths': (
            # Windows
            ['./testdir\\subdir1\\a.c',
             './testdir\\subdir3\\subsubdir1\\b.c',
             './testdir\\subdir5\\a.c',
             './testdir\\t1.c'],
            # Linux
            ['./testdir/subdir1/a.c',
             './testdir/subdir3/subsubdir1/b.c',
             './testdir/subdir5/a.c',
             './testdir/t1.c'])
    },

    {
        'suffix': ".gitkeep",
        'path': "./testdir",
        'file_paths': (
            ['./testdir\\subdir2\\.gitkeep', './testdir\\subdir4\\.gitkeep'],
            ['./testdir/subdir2/.gitkeep', './testdir/subdir4/.gitkeep'])
    },

    {
        'suffix': ".c",
        'path': "./testdir/subdir5",
        'file_paths': (
            ['./testdir/subdir5\\a.c'],
            ['./testdir/subdir5/a.c'])
    }
]


@pytest.mark.parametrize("dct", TEST_NORMAL)
def test_normal(dct):
    assert sorted(find_files(dct['suffix'], dct['path'])) in dct['file_paths']


def test_edge():
    suffix = ".c"
    path = "./crazydir"
    with pytest.raises(IOError,
                       match="No such directory .* or it points to a file."):
        find_files(suffix, path)

    suffix = ".h"
    path = './testdir/t1.h'
    with pytest.raises(IOError,
                       match="No such directory .* or it points to a file."):
        find_files(suffix, path)


if __name__ == '__main__':
    pytest.main()
