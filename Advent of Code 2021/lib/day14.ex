defmodule Day14 do
  def step(string, transforms) do
    0..(String.length(string) - 2)
    |> Enum.map(fn i ->
      pair =
        string
        |> String.slice(i..(i + 1))

      String.at(string, i) <> Map.get(transforms, pair, "")
    end)
    |> Enum.concat([String.at(string, -1)])
    |> Enum.join()
  end

  def n_steps(string, transforms, n) do
    IO.inspect(n, label: :steps_remaining)

    if n <= 0 do
      string
    else
      n_steps(step(string, transforms), transforms, n - 1)
    end
  end

  def part(string, transforms, steps) do
    freqs =
      string
      |> Day14.n_steps(transforms, steps)
      |> String.to_charlist()
      |> Enum.frequencies()
      |> Map.values()

    Enum.max(freqs) - Enum.min(freqs)
  end
end

{:ok, file} = File.read("inputs/day14.in")

base =
  file
  |> String.split("\n", trim: true)
  |> Enum.at(0)

transforms =
  file
  |> String.split("\n", trim: true)
  |> Enum.slice(1..-1)
  |> Enum.map(fn s ->
    [pair, new] =
      s
      |> String.split(" -> ")

    %{pair => new}
  end)
  |> Enum.reduce(&Map.merge/2)

base
|> Day14.part(transforms, 10)
|> IO.inspect(label: "Part 1")

base
|> Day14.part(transforms, 40)
|> IO.inspect(label: "Part 2")
