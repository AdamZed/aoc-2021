defmodule Solve do
    def part1(data) do
        base4s = for entry <- data,
            part = entry |> Enum.at(1),
            parts = String.split(part, " "),
            signals <- parts,
            String.length(signals) in [2, 3, 4, 7],
            do: signals
        base4s |> length

    end

    def part2(data) do
        IO.puts data
    end

    def read_input(fname) do
        File.read!(fname)
            |> String.trim
            |> String.split("\n")
            |> Enum.map(fn s -> String.split(s, " | ") end)
    end

end

data = Solve.read_input("input.txt")

IO.puts "Part 1: #{Solve.part1(data)}"
# IO.puts "Part 2: #{Solve.part2(data)}"