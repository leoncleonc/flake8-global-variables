import ast


_GV400 = '_G400: Found global variable'


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.errors = []

    def visit_Global(self, node):
        for name in node.names:
            if not name.isupper():
                self.errors.append((node.lineno, node.col_offset, _GV400))
                self.generic_visit(node)

    def visit_Assign(self, node):
        if node.col_offset == 0:
            for target in node.targets:
                if hasattr(target, 'id') and not target.id.isupper():
                    self.errors.append((node.lineno, node.col_offset, _GV400))
                    self.generic_visit(node)