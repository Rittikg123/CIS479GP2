# CIS479GP2

1. player function - it takes the count of x and o and if x sum matches with o sum, that means it's x's turn next, or else it's o's turn.
2. actions function - First, a set is created. Then nested loop is used to check if the section of the board is empty, and if it is, it adds the i and j into the set that was created. 
3. result function - First, i and j was provided with the action parameter. Then a deepcopy of the board parameter was saved in another variable named new_board. Then another variable named current_player was made to see whose turn it was next. Then the section of the new_board was provided with current_player. 
4. winner function - For loops were created to check the row and column. Then for loop was created to check the diagonal sides. If no winner is found, return none. 
5. terminal function - First, it returned true if theres a winner. Then checked to see if row is empty and if it does, it returns false. If no empty cells are found and there's no winner, it's a tie. 
6. utility function - If statements were created to see if winner is X or O. 
7. minimax function - it uses recursive to check all the action a player will take and finds the best path based on that. 