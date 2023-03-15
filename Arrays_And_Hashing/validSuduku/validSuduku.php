<?php

function isValidSudoku($board) {

    for ($i=0; $i<9; $i++){
        $currentRow = [];
        $currentColumn = [];
        $currentSubBoard = [];
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

            echo 'row value > '. $board[$i][$j] . '        i='.$i.'  j='.$j . "\n";
            echo 'column value > '. $board[$j][$i] .'     j='.$j.'  i='.$i . "\n";
            echo 'subBoard value > '. $board[$subBoardI][$subBoardJ] .'        i='.$subBoardI.'  j='.$subBoardJ . "\n";

            if ($board[$i][$j] !== '.' || $board[$j][$i] !== '.' || $board[$subBoardI][$subBoardJ] !== '.'){

                if ($board[$i][$j] !== '.' && !in_array($board[$i][$j], $currentRow))
                    $currentRow[] = $board[$i][$j];
                else {
                    echo 'invalid row > ';
                    print_r($board[$i][$j] !== '.');
                    return false;
                }

                if ($board[$j][$i] !== '.' && !in_array($board[$j][$i], $currentColumn))
                    $currentColumn[] = $board[$j][$i];
                else {
                    echo 'invalid column';
                    return false;
                }

                if ($board[$subBoardI][$subBoardJ] !== '.' && !in_array($board[$subBoardI][$subBoardJ], $currentSubBoard)){
                    $currentSubBoard[] = $board[$subBoardI][$subBoardJ];
                } else {
                    echo 'invalid box';
                    return false;
                }
            }
            echo 'row > ';
            print_r($currentRow);
            echo "\n";

            echo 'column > ';
            print_r($currentColumn);
            echo "\n";

            echo 'box > ';
            print_r($currentSubBoard);
            echo "\n\n";
        }
        echo "\n\n";
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