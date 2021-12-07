package day04;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;

public class Day4 {

    public static long part1(Board[] boards, int[] calls) {
        for (int call : calls) {
            for (Board board : boards) {
                if (board.mark(call))
                    return board.score(call);
            }
        }
        return 0;
    }
    public static long part2(Board[] boards, int[] calls) {
        for (int call : calls) {
            for (Board board : boards)
                board.mark(call);
            if (boards.length > 1) {
                boards = Arrays.asList(boards).stream().filter(e -> !e.isWon).toArray(Board[]::new);
                continue;
            }
            if (boards[0].isWon) return boards[0].score(call);
        }
        return 0;
    }
    
    public static void main(String args[]) throws IOException {
        String data = new String(Files.readAllBytes(Paths.get("./day04/input.txt")), StandardCharsets.UTF_8);

        String[] chunks = data.split("\n\n");
        Board[] boards = new Board[chunks.length - 1];

        int[] calls = Arrays.asList(chunks[0].split(",")).stream().mapToInt(Integer::parseInt).toArray();

        for (int i = 1; i < chunks.length; i++) {
            boards[i-1] = new Board(chunks[i]);
        }

        System.out.println("Part 1: " + part1(boards, calls));
        System.out.println("Part 2: " + part2(boards, calls));

    }
}

class Board {
    private static int GRID_SIZE = 5;
    int[][] board;
    boolean isWon = false;

    Board(String entries) {
        int row = 0;
        board = new int[GRID_SIZE][GRID_SIZE];
        for (String ln : entries.split("\n"))
            board[row++] = Arrays.asList(ln.split(" ")).stream().filter((e) -> !e.strip().equals("")).mapToInt(Integer::parseInt).toArray();
    }

    boolean mark(int call) {
        for (int i = 0; i < GRID_SIZE; i++) {
            for (int j = 0; j < GRID_SIZE; j++) {
                if (board[i][j] == call) {
                    board[i][j] = -1;
                    return checkWin();
                }
            }
        }
        return false;
    }

    boolean checkWin() {
        for(int i = 0; i < GRID_SIZE; i++) {
            boolean isWinH = true, isWinV = true;
            for(int j = 0; j < GRID_SIZE; j++) {
                isWinH &= board[i][j] == -1;
                isWinV &= board[j][i] == -1;
            }
            if (isWinH || isWinV) {
                isWon = true;
                return true;
            }
        }
        return false;
    }

    long score(int call) {
        long sum = 0;
        for(int i = 0; i < GRID_SIZE; i++) {
            for(int j = 0; j < GRID_SIZE; j++) {
                if (board[i][j] != -1)
                    sum += board[i][j];
            }
        }
        return sum*call;
    }
}