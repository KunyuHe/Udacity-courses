# Problem Statement

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by string representing their ids.

```python
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
```

Write a function that provides an efficient look up of whether the user is in a group.

# Design

We can easily solve this problem with recursion, as a group can consist of user(s) and group(s) themselves. To check if a user is in a group, we can first iterate through its user list. If we do not find the user there, we can apply the same function to all of its sub groups. If none of those returns `True`, we can safely say the user is not in the group and return `False`.

The *time complexity* of this approach in the worst case is `O(n)` as we might have to iterate through all the input elements but it would not be more than once. *Space complexity* would be `O(1)` as we does not create any extra data structures.

# Files

- [main.py](main.py): contains the `is_user_in_group(user, group)` function.
- [group.py](group.py): holds the `Group()` class from skeleton.
- [test.py](test.py): contains test cases for the function implementation.