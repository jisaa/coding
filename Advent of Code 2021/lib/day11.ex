defmodule Day11 do
  def next_step(octopi) do
    octopi
    |> Day11.increase_energy()
    |> Day11.blink_all()
  end

  def increase_energy(octopi) do
    0..(Enum.count(octopi) - 1)
    |> Enum.map(fn i ->
      0..(Enum.count(Enum.at(octopi, 0)) - 1)
      |> Enum.map(fn j ->
        [energy, blinks] = Enum.at(Enum.at(octopi, i), j)
        [energy + 1, blinks]
      end)
    end)
  end

  def blink_all(octopi) do
    energies =
      octopi
      |> Enum.flat_map(fn row ->
        row
        |> Enum.flat_map(fn [energy, _blinks] ->
          [energy]
        end)
      end)

    if Enum.any?(energies, fn x -> x > 9 end) do
      index = Enum.find_index(energies, fn x -> x > 9 end)

      i = div(index, Enum.count(octopi))

      j = rem(index, Enum.count(octopi))

      octopi
      |> Day11.blink(i, j)
      |> Day11.blink_all()
    else
      octopi
    end
  end

  def blink(octopi, i, j) do
    # set energy to 0
    [_energy, blinks] = Enum.at(Enum.at(octopi, i), j)

    octopi
    |> Day11.replace(i, j, [0, blinks + 1])
    # increase neighbours energy if >0
    |> Day11.check(i + 1, j)
    |> Day11.check(i - 1, j)
    |> Day11.check(i + 1, j + 1)
    |> Day11.check(i - 1, j + 1)
    |> Day11.check(i, j + 1)
    |> Day11.check(i + 1, j - 1)
    |> Day11.check(i - 1, j - 1)
    |> Day11.check(i, j - 1)
  end

  def check(octopi, i, j) do
    if i < 0 or i >= Enum.count(octopi) or j < 0 or j >= Enum.count(Enum.at(octopi, 0)) do
      octopi
    else
      new_octopus = Day11.increase(Enum.at(Enum.at(octopi, i), j))
      Day11.replace(octopi, i, j, new_octopus)
    end
  end

  def increase(octopus) do
    [energy, blinks] = octopus

    if energy > 0 do
      [energy + 1, blinks]
    else
      octopus
    end
  end

  def replace(octopi, a, b, new_octopus) do
    0..(Enum.count(octopi) - 1)
    |> Enum.map(fn i ->
      0..(Enum.count(Enum.at(octopi, 0)) - 1)
      |> Enum.map(fn j ->
        if i == a and j == b do
          new_octopus
        else
          Enum.at(Enum.at(octopi, i), j)
        end
      end)
    end)
  end

  def print(octopi, label \\ "") do
    octopi
    |> Enum.map(fn row ->
      Enum.map(row, fn t ->
        Enum.at(t, 0)
      end)
    end)
    |> IO.inspect(label: label)

    octopi
  end

  def n_steps(octopi, n) do
    if n == 0 do
      octopi
    else
      octopi
      |> Day11.next_step()
      |> Day11.n_steps(n - 1)
    end
  end

  def find_sync(octopi, steps \\ 0) do
    if octopi
       |> Enum.flat_map(& &1)
       |> Enum.flat_map(fn [energy, _blinks] -> [energy] end)
       |> Enum.frequencies()
       |> Enum.count() > 1 do
      octopi
      |> Day11.next_step()
      |> Day11.find_sync(steps + 1)
    else
      steps
    end
  end
end

{:ok, file} = File.read("inputs/day11.in")

octopi =
  file
  |> String.split("\n", trim: true)
  |> Enum.map(fn s ->
    s
    |> String.split("", trim: true)
    |> Enum.map(fn x ->
      # current energy, total blinks
      [String.to_integer(x), 0]
    end)
  end)

octopi
|> Day11.n_steps(100)
|> Enum.flat_map(& &1)
|> Enum.map(fn [_, x] -> x end)
|> Enum.sum()
|> IO.inspect(label: "Part 1")

octopi
|> Day11.find_sync()
|> IO.inspect(label: "Part 2")
