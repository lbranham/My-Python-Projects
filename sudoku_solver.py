import math
import time

def main():
  
  sudokutest = [
      [0,0,0,0,9,0,0,4,0], 
      [0,1,0,2,4,0,7,0,9], 
      [0,0,0,7,5,0,0,2,6],
      [0,5,1,0,0,2,0,0,4],
      [7,0,2,4,0,5,9,0,1],
      [9,0,0,3,0,0,5,8,0],
      [5,9,0,0,2,7,0,0,0],
      [2,0,3,0,1,9,0,5,0],
      [0,6,0,0,3,0,0,0,0]
  ]
  
    solved_sudoku = sudoku_solver(sudokutest)
    if ( not valid_sudoku(solved_sudoku)):

        i = 0
        while i < 9:
            row = solved_sudoku[i]
            print("{} {} {} | {} {} {} | {} {} {}".format(*row))
            if (((i + 1) % 3) == 0) and i != 8:
                print("---------------------")
            i += 1
    else:
        print("Solved")

if __name__ == "__main__":
    main()
    
    

def count_blanks(puzzle):
    zero_count = 0
    for row in puzzle:
        for digit in row:
            if (digit == 0):
                zero_count += 1
    return zero_count

def get_boxes(puzzle):
    
    boxes = [[[],[],[]],[[],[],[]],[[],[],[]],]
    i = 0
    
    while i < 9:
        row = puzzle[i]
        j = 0
        
        while j < 9:
            box_row = math.floor((i + 1) / 3 - .1)
            box_column = math.floor((j + 1) / 3 - .1)
            boxes[box_row][box_column].append(row[j])
            j += 1
            
        i += 1
        
    return boxes

def sudoku_solver(puzzle):
    possible_digits = [1,2,3,4,5,6,7,8,9]
    """
    Takes an unsolved sudoku puzzle as a 2d array and outputs the solution as a 2d array where the sublists contain
    the rows of the puzzle. Blank spaces are represented by zeros
    [[0,0,0,0,9,0,0,4,0], [0,1,0,2,4,0,7,0,9], [0,0,0,7,5,0,0,2,6]...]
    represents:
    _ _ _ | _ 9 _ | _ 4 _
    _ 1 _ | 2 4 _ | 7 _ 9
    _ _ _ | 7 5 _ | _ 2 6   
    """
    
    start_time = time.time()
    
    blanks = count_blanks(puzzle)
    columns = [list(x) for x in zip(*puzzle)]
    
        
    boxes = get_boxes(puzzle)
    sudoku = puzzle

    while (blanks > 0):
        if (time.time() - start_time > .3):
            break 
        i = 0
        while i < 9:
            row = puzzle[i]        
            j = 0
            while j < 9:
                box_row = math.floor((i + 1) / 3 - .1)
                box_column = math.floor((j + 1) / 3 - .1)
                box = boxes[box_row][box_column]
                used_digits = row + list(columns[j]) + box
            
                available_digits = list(set(possible_digits) - set(used_digits))

                if ((len(available_digits) == 1) and row[j] == 0):

                    row[j] = available_digits[0]
                    columns[j][i] = available_digits[0]
                    box.append(available_digits[0])
                    sudoku[i][j] = (available_digits[0])
                
                j += 1
            i += 1
            blanks = count_blanks(puzzle)
    return sudoku


def sum_of_array(array):
    """Returns the sum of an array"""
    running_total = 0
    for i in array:
        running_total += i
    return running_total
        

def valid_sudoku(puzzle):
    for row in puzzle:
        row_total = sum_of_array(row)
        if row_total != 45:
            return False
    columns = [list(x) for x in zip(*puzzle)]
    for column in columns:
        column_total = sum_of_array(column)
        if column_total != 45:
            return False
    boxes = get_boxes(puzzle)
    
    for box_row in boxes:
        for box in box_row:
            box_total = sum_of_array(box)
            if box_total != 45:
                return False
    return True
    

        
