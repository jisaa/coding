defmodule Day6 do
  def age(fish) do
    if fish > 0 do
      [fish - 1]
    else
      [6, 8]
    end
  end

  def next_naive(fishes, steps \\ 0) do
    if steps > 0 do
      next_naive(
        fishes
        |> Enum.map(&Day6.age/1)
        |> Enum.flat_map(& &1),
        steps - 1
      )
    else
      fishes
    end
  end

  def to_enum(fishes_freq) do
    [
      Map.get(fishes_freq, 0, 0),
      Map.get(fishes_freq, 1, 0),
      Map.get(fishes_freq, 2, 0),
      Map.get(fishes_freq, 3, 0),
      Map.get(fishes_freq, 4, 0),
      Map.get(fishes_freq, 5, 0),
      Map.get(fishes_freq, 6, 0),
      Map.get(fishes_freq, 7, 0),
      Map.get(fishes_freq, 8, 0)
    ]
  end

  def next_with_frequencies(fishes, steps \\ 0) do
    if steps > 0 do
      next_fishes = [
        Enum.at(fishes, 1),
        Enum.at(fishes, 2),
        Enum.at(fishes, 3),
        Enum.at(fishes, 4),
        Enum.at(fishes, 5),
        Enum.at(fishes, 6),
        Enum.at(fishes, 7) + Enum.at(fishes, 0),
        Enum.at(fishes, 8),
        Enum.at(fishes, 0)
      ]

      next_with_frequencies(
        next_fishes,
        steps - 1
      )
    else
      fishes
    end
  end
end

{:ok, file} = File.read("inputs/day6.in")

fishes =
  file
  |> String.split(",", trim: true)
  |> Enum.map(&String.to_integer/1)
  |> Enum.frequencies()
  |> Day6.to_enum()

fishes
|> Day6.next_with_frequencies(80)
|> Enum.sum()
|> IO.inspect(label: "Part 1")

fishes
|> Day6.next_with_frequencies(256)
|> Enum.sum()
|> IO.inspect(label: "Part 2")
