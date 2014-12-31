
class Node(object):
  def __init__(self, altitude):
    self.altitude = altitude
    self.adjacents = []
    self.is_destination = False

  def add_adjacent(self, node):
    self.adjacents.append(node)

  def remove_unvisitable_adjacents(self):
    visitables = [x for x in self.adjacents if x.is_visitable(from_=self)]
    self.adjacents = visitables

  def is_visitable(self, from_):
    return (from_.altitude > self.altitude)


def parse_and_get_first_node(raw):
  rows = raw.splitlines()

  dimension = rows.pop(0)
  dimension = dimension.split(' ')
  height = int(dimension[0])
  width = int(dimension[1])

  for y in range(0, height):
    row = rows[y] = rows[y].split(' ')
    for x in range(0, width):
      altitude = row[x] = int(row[x])
      row[x] = node = Node(altitude)

      if x > 0:
        left = row[x-1]
        node.add_adjacent(left)
        left.add_adjacent(node)

      if y > 0:
        upper = rows[y-1][x]
        node.add_adjacent(upper)
        upper.add_adjacent(node)

  flattened = [item for sublist in rows for item in sublist] # googled how to
  [node.remove_unvisitable_adjacents() for node in flattened]

  first_node = flattened[0]
  last_node = flattened[-1]
  last_node.is_destination = True

  return first_node

# visit recursively and return possible paths' count within its trials
def visit(node, path):
  if node in path:
    return 0
  if node.is_destination:
    # found possible path
    return 1
  count = 0
  path.append(node)
  for adjacent in node.adjacents:
    count += visit(adjacent, path)
  # dead end
  path.pop()
  return count


if __name__ == '__main__':
  raw = []
  while True:
    try:
      line = raw_input()
      if line:
        raw.append(line)
      else:
        break
    except EOFError:
      break
  raw = '\n'.join(raw)

  first_node = parse_and_get_first_node(raw)

  path = []
  count = visit(first_node, path)
  print (count)
