# Problem Statement

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c". Note that a path may contain further subdirectories and those subdirectories may also contain further subdirectories. There are no limits to the depth of the subdirectories can be.

Here is an example of a test directory listing, which can be downloaded [here](https://s3.amazonaws.com/udacity-dsand/testdir.zip):

```bash
./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
```

**Note:** `os.walk()` is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use `os.walk()`.

# Design

Since a path may contain further subdirectories and those subdirectories may also contain further subdirectories, it's clear that recursion can be a good implementation. The solution would traverse each subdirectory exactly once, hence its *time complexity* should be `O(n)`. Its *space complexity* is `O(n)` as we create a list to hold the file names that have the specified suffix and its length is dependent on input size linearly. See below for the file structures.

However, when the recursion is very deep, the time of each level delivering its result back up the call stack would matter. Also, recursion might not be ideal since there are no limits to the depth of the subdirectories can be and the maximum recursion depth in Python is rather conservative. Our solution might crash with a much deeply nested directory structure.

Programming defensively, we need to catch degenerate cases where the path to the top of the directory structure does not exist or does not point to a directory.

# Files

- [main.py](main.py): contains function `find_files(suffix, path)` that returns a list of relative paths to files under directory `path` whose names end with `suffix`. The script takes `--suffix` and `--path` as argument in console.
- [test.py](test.py): contains test cases for the `find_files(suffix, path)` implementation.

