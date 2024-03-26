class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    node = self.root
    nodes_to_visit = [node]

    while len(nodes_to_visit) > 0:
      if node['id'] == id:
        return node
      node = nodes_to_visit.pop(0)
      nodes_to_visit = node['children'] + nodes_to_visit
    return None
