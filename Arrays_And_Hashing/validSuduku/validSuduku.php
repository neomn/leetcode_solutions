<?php

function isValidSudoku($board) {
    $currentRow = [];
    $currentColumn = [];
    $subBoardIsValid = false;

    for ($i=0; $i<9; $i++){
        for ($j=0; $j<9; $j++){
            if ($board[$i][$j] !== '.' && $board[$j][$i] !== '.'){

                if (!in_array($board[$i][$j], $currentRow))
                    $currentRow[] = $board[$i][$j];
                else echo "invalid row \n";

                if (!in_array($board[$j][$i], $currentColumn))
                    $currentColumn[] = $board[$j][$i];
                else echo "invalid column\n";
            }
        }
        $currentRow = [];
        $currentColumn = [];
    }
    return true;
}



$board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]];

print_r(isValidSudoku( $board ));