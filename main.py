from dataclasses import dataclass, field

@dataclass
class Cell:
    x: int
    y: int
    north: bool = field(default=True)
    east: bool = field(default=True)
    south: bool = field(default=True)
    west: bool = field(default=True)
    
def set_vertices(lines: list[str], cells: list[Cell]):
    assert len(lines) == 3
    num_cells_in_line = len(lines[0])//3
    assert len(cells) == num_cells_in_line
    top_line, middle_line, bottom_line = lines
    for i in range(num_cells_in_line):
        _, n1, n2 = top_line[i*3:i*3+3]
        if n1 == n2 == '-':
            cells[i].north = False
        w, _, _, e = middle_line[i*3:i*3+4]
        if e == '|':
            cells[i].east = False
        if w == '|':
            cells[i].west = False
        _, s1, s2 = bottom_line[i*3:i*3+3]
        if s1 == s2 == '-':
            cells[i].south = False
    return cells

if __name__ == '__main__':
    with open('simple-maze-1.txt', 'r') as file:
        file_data = file.read()
    lines = file_data.split('\n')
    
    cells = []
    num_cells_per_row = len(lines[0])//3
    num_cells_per_col = len(lines)//2
    for i in range(num_cells_per_col):
        these_lines = lines[i*3 - i:i*3 + 3 - i]
        these_cells = [Cell(c,i) for c in range(num_cells_per_row)]
        these_cells = set_vertices(these_lines, these_cells)
        cells += these_cells
    print(cells)
    
