def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True

    sub_groups = group.get_groups()
    if not sub_groups:
        return False

    for sub_group in sub_groups:
        return is_user_in_group(user, sub_group)

    return False


if __name__ == '__main__':
    pass
