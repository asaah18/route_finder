class Stack:
    """a class to represent stack data structure with no redundant in stack"""
    stack = []

    def unique_push(self, item):
        """push a node into stack if it's not there

        :parameter item : the node to add to stack
        """
        if item not in self.stack:
            self.stack.append(item)

    def pop(self):
        """:return item at the top of stack or declare error."""
        return self.stack.pop()

    def is_empty(self) -> bool:
        """:return boolean : True or False """
        return not self.stack

    def display(self):
        """display the content of stack in CLI"""
        print("stack:", self.stack, ">top")
