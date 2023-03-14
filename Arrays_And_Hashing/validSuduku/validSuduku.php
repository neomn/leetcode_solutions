<?php

function isValidSudoku($board) {
    $currentRow = [];
    $currentColumn = [];
    $currentSubBoard = [];

    for ($i=0; $i<9; $i++){
        for ($j=0; $j<9; $j++){

            $subBoardI = floor($j/3) + floor($i/3)*3 ;
            $subBoardJ = $j%3 + floor($i/3)*3 ;

            echo $subBoardI . "  ";
            echo $subBoardJ . "\n";

//            if ($board[$i][$j] !== '.' && $board[$j][$i] !== '.' && $board[$subBoardI][$subBoardJ] !== '.'){
//
//                if (!in_array($board[$i][$j], $currentRow))
//                    $currentRow[] = $board[$i][$j];
//                else echo "invalid row \n";
//
//                if (!in_array($board[$j][$i], $currentColumn))
//                    $currentColumn[] = $board[$j][$i];
//                else echo "invalid column\n";
//
//                if (!in_array($currentSubBoard, $board[$subBoardI][$subBoardJ])){
//                    $currentSubBoard[] = $board[$subBoardI][$subBoardJ];
//                } else echo "invalid subBoard\n";
//
//            }
        }
        $currentRow = [];
        $currentColumn = [];
        $currentSubBoard = [];

        echo "\n";
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