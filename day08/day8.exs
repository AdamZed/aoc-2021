defmodule Solve do
    # maps num_segments -> number
    @base_segments %{2 => 1, 3 => 7, 4 => 4, 7 => 8}

    def read_input(fname) do
        data = File.read!(fname)
            |> String.trim
            |> String.split("\n")
            |> Enum.map(&(String.split(&1, " | ")))
        for [left, right] <- data, do: [String.split(left, " "), String.split(right, " ")]
    end

    def part1(data) do
        base4s = for entry <- data,
            outputs = entry |> Enum.at(1),
            signal <- outputs,
            String.length(signal) in Map.keys(@base_segments),
            do: signal
        base4s |> length 
    end

    def part2(data) do
        entries = for entry <- data,
            [inps, outs] = entry,
            base_four = get_base_four(inps),
            decoded = decode_inputs(base_four, inps),
            do: decode_output(decoded, outs)
        entries |> Enum.sum
    end

    defp get_base_four(from_input) do
        for signal <- from_input |> Enum.map(&(sort(&1))) |> Enum.uniq,
            len = String.length(signal),
            len in Map.keys(@base_segments),
            into: %{},
            do: {signal, @base_segments[len]}
    end

    defp decode_inputs(codes, input) do
        rev_codes = for {segs, num} <- codes, into: %{}, do: {num, segs}
        decode_input(input, codes, rev_codes)
    end

    defp decode_input([head | tail], codes, rev_codes) do
        head = sort(head)
        codes = case String.length(head) do
            5 -> cond do
                    isect_len(rev_codes[1], head) == 2 ->
                        Map.put(codes, head, 3)
                    isect_len(rev_codes[4], head) == 3 ->
                        Map.put(codes, head, 5)
                    true -> Map.put(codes, head, 2)
                end
            6 -> cond do
                    isect_len(rev_codes[1], head) != 2 ->
                        Map.put(codes, head, 6)
                    isect_len(rev_codes[4], head) == 4 ->
                        Map.put(codes, head, 9)
                    true -> Map.put(codes, head, 0)
                end
            _ -> codes
            end
        decode_input(tail, codes, rev_codes)
    end
    defp decode_input([], codes, _), do: codes

    defp decode_output(codes, output) do
        digits = for {signal, i} <- output |> Enum.map(&(sort(&1))) |> Enum.with_index,
            val = codes[signal],
            do: val * 10 ** (3-i)
        digits |> Enum.sum
    end

    defp sort(str) do
        str |> String.to_charlist
            |> Enum.sort
            |> List.to_string
    end

    defp isect_len(str1, str2) do
        ar1 = str1 |> String.to_charlist
        ar2 = str2 |> String.to_charlist
        ar1 -- (ar1 -- ar2) |> length
    end
end

data = Solve.read_input("input.txt")

IO.puts "Part 1: #{Solve.part1(data)}"
IO.puts "Part 2: #{Solve.part2(data)}"