import random
import sys

class Cell:
  def __init__(self):
    self.is_mine = False
    self.revealed = False

def generate_board(num_mines):
  board = []
  for _ in range(3):
    row = []
    for _ in range(3):
      row.append(Cell())
    board.append(row)

  for _ in range(num_mines):
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    while board[row][col].is_mine:
      row = random.randint(0, 2)
      col = random.randint(0, 2)
    board[row][col].is_mine = True

  return board

def display_board(board):
  for row in board:
    for cell in row:
      if cell.revealed:
        if cell.is_mine:
          print("X", end=" ")
        else:
          print("0", end=" ") 
      else:
        print("?", end=" ")
    print()

def handle_turn(board):
  while True:
    try:
      row = int(input("Enter row (1-3): ")) - 1
      col = int(input("Enter column (1-3): ")) - 1
      if 0 <= row < 3 and 0 <= col < 3:
        break
      else:
        print("Invalid input, values must be between 1 and 3")
    except ValueError:
        print("Invalid input, Adios.")
        sys.exit()  

  cell = board[row][col]
  cell.revealed = True
  if cell.is_mine:
    print("Congratulations, you found the mine")
    display_board(board)
    return False
  else:
    print("Safe, next...")
  return True

def reveal_all_mines(board):
  for row in board:
    for cell in row:
      cell.revealed = True  
      
def main():
  num_mines = 1  
  board = generate_board(num_mines)
  game_over = False

  while not game_over:
    display_board(board)
    game_over = not handle_turn(board)

  if not game_over:
    print("Tough luck!")
    
main()
