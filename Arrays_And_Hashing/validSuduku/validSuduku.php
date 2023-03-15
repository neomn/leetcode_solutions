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
        }
    }
    return true;
}


$board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]];

print_r(isValidSudoku($board));