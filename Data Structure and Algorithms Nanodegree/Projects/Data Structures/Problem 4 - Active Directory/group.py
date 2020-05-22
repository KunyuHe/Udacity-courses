class Group:
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


def create_mad_men_tree():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_users = ["Tammy", "Sally", "Bobby", "Kevin"]
    for sub_child_user in sub_child_users:
        sub_child.add_user(sub_child_user)

    child_users = ["Pete", "Trudy", "Don", "Betty", "Roger", "Joan"]
    for child_user in child_users:
        child.add_user(child_user)

    parent_users = ["Archie", "Abigail", "Tom", "Gail"]
    for parent_user in parent_users:
        parent.add_user(parent_user)

    child.add_group(sub_child)
    parent.add_group(child)
    return parent, child, sub_child


if __name__ == '__main__':
    pass
