defmodule Day8 do
  def signals(line) do
    line
    |> String.split(" | ")
    |> Enum.at(0)
    |> String.split(" ")
  end

  def output(line) do
    line
    |> String.split(" | ")
    |> Enum.at(1)
    |> String.split(" ")
  end

  def find_by_freq(freqs, n, exclude \\ "") do
    "abcdefg"
    |> String.split("", trim: true)
    |> Enum.filter(fn x -> Map.get(freqs, x) == n end)
    |> Enum.filter(fn x -> x != exclude end)
    |> Enum.at(0)
  end

  def get_a(signals) do
    seven =
      signals
      |> Enum.filter(fn x -> String.length(x) == 3 end)
      |> Enum.at(0)
      |> String.split("", trim: true)

    one =
      signals
      |> Enum.filter(fn x -> String.length(x) == 2 end)
      |> Enum.at(0)
      |> String.split("", trim: true)

    seven
    |> Enum.filter(fn x -> not Enum.member?(one, x) end)
    |> Enum.at(0)
  end

  def get_d(signals, b, c, f) do
    four =
      signals
      |> Enum.filter(fn x -> String.length(x) == 4 end)
      |> Enum.at(0)
      |> String.split("", trim: true)

    four
    |> Enum.filter(fn x -> not Enum.member?([b, c, f], x) end)
    |> Enum.at(0)
  end

  def decode(line) do
    signals = Day8.signals(line)

    freqs =
      signals
      |> Enum.join()
      |> String.split("", trim: true)
      |> Enum.frequencies()

    a = Day8.get_a(signals)

    b = Day8.find_by_freq(freqs, 6)
    c = Day8.find_by_freq(freqs, 8, a)

    e = Day8.find_by_freq(freqs, 4)
    f = Day8.find_by_freq(freqs, 9)

    d = Day8.get_d(signals, b, c, f)
    g = Day8.find_by_freq(freqs, 7, d)

    nums = [
      Enum.join(Enum.sort([a, b, c, e, f, g])),
      Enum.join(Enum.sort([c, f])),
      Enum.join(Enum.sort([a, c, d, e, g])),
      Enum.join(Enum.sort([a, c, d, f, g])),
      Enum.join(Enum.sort([b, c, d, f])),
      Enum.join(Enum.sort([a, b, d, f, g])),
      Enum.join(Enum.sort([a, b, d, e, f, g])),
      Enum.join(Enum.sort([a, c, f])),
      Enum.join(Enum.sort([a, b, c, d, e, f, g])),
      Enum.join(Enum.sort([a, b, c, d, f, g]))
    ]

    outputs = Day8.output(line)

    outputs
    |> Enum.map(fn x ->
      x =
        x
        |> String.split("")
        |> Enum.sort()
        |> Enum.join()

      Enum.find_index(nums, fn y -> y === x end)
      |> Integer.to_string()
    end)
    |> Enum.join()
    |> String.to_integer()
  end
end

{:ok, file} = File.read("inputs/day8.in")

lines =
  file
  |> String.split("\n", trim: true)

lines
|> Enum.map(&Day8.output/1)
|> Enum.flat_map(& &1)
|> Enum.map(&String.length/1)
|> Enum.filter(fn x ->
  Enum.member?([2, 3, 4, 7], x)
end)
|> Enum.count()
|> IO.inspect(label: "Part 1")

lines
|> Enum.map(&Day8.decode/1)
|> Enum.sum()
|> IO.inspect(label: "Part 2")
