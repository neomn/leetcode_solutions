<?php

function isValidSudoku($board) {
    $currentRow = [];
    $currentColumn = [];
    $currentSubBoard = [];

    for ($i=0; $i<9; $i++){
        for ($j=0; $j<9; $j++){

            $subBoardI = floor($j/3) + floor($i/3)*3 ;
            $subBoardJ = $j%3 + floor($i/3)*3 ;

            echo 'first condition > ';
            print_r($board[$i][$j] !== '.' );
            echo "\n";

            echo 'second condition > ';
            print_r($board[$j][$i] !== '.');
            echo "\n";

            echo 'third condition > ';
            print_r($board[$subBoardI][$subBoardJ] !== '.');
            echo "\n";

            echo 'board row value > '. $board[$i][$j] . '        i='.$i.'  j='.$j . "\n";
            echo 'board column value > '. $board[$j][$i] .'     i='.$i.'  j='.$j . "\n";
            echo 'sub board value > '. $board[$subBoardI][$subBoardJ] .'        i='.$i.'  j='.$j . "\n\n";

            if ($board[$i][$j] !== '.' && $board[$j][$i] !== '.' && $board[$subBoardI][$subBoardJ] !== '.'){

                if (!in_array($board[$i][$j], $currentRow))
                    $currentRow[] = $board[$i][$j];
                else echo "invalid row \n";

                if (!in_array($board[$j][$i], $currentColumn))
                    $currentColumn[] = $board[$j][$i];
                else echo "invalid column\n";

                if (!in_array($board[$subBoardI][$subBoardJ], $currentSubBoard)){
                    $currentSubBoard[] = $board[$subBoardI][$subBoardJ];
                } else echo "invalid subBoard\n";

            }
        }
        $currentRow = [];
        $currentColumn = [];
        $currentSubBoard = [];

        echo "\n\n";
    }
    return true;
}



$board = [["5","3",".",".","7",".",".",".","."]
         ,["6","6",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]];

print_r(isValidSudoku( $board ));