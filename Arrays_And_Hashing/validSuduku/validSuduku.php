<?php

function isValidSudoku($board)
{
    for ($i = 0; $i < 9; $i++) {
        $currentRow = [];
        $currentColumn = [];
        $currentSubBoard = [];
        for ($j = 0; $j < 9; $j++) {
            $subBoardI = floor($j / 3) + floor($i / 3) * 3;
            $subBoardJ = $j % 3 + floor($i / 3) * 3;
            echo $subBoardI,$subBoardJ;
            echo "\n";

            if ($board[$i][$j] !== '.')
                if (!in_array($board[$i][$j], $currentRow))
                    $currentRow[] = $board[$i][$j];
                else return false;

            if ($board[$j][$i] !== '.')
                if (!in_array($board[$j][$i], $currentColumn))
                    $currentColumn[] = $board[$j][$i];
                else return false;

            if ($board[$subBoardI][$subBoardJ] !== '.')
                if (!in_array($board[$subBoardI][$subBoardJ], $currentSubBoard))
                    $currentSubBoard[] = $board[$subBoardI][$subBoardJ];
                else return false;

//            echo $subBoardI,$subBoardJ;
//            print_r($currentSubBoard);
//            echo "\n";
        }
        echo "\n\n";
    }
    return true;
}


$board = [[".",".",".",".","5",".",".","1","."],
          [".","4",".","3",".",".",".",".","."],
          [".",".",".",".",".","3",".",".","1"],
          ["8",".",".",".",".",".",".","2","."],
          [".",".","2",".","7",".",".",".","."],
          [".","1","5",".",".",".",".",".","."],
          [".",".",".",".",".","2",".",".","."],
          [".","2",".","9",".",".",".",".","."],
          [".",".","4",".",".",".",".",".","."]];

print_r(isValidSudoku($board));