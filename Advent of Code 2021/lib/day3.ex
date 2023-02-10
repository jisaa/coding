defmodule Day3 do
  def mostCommon(numbers, pos) do
    zeroes =
      numbers
      |> Enum.map(fn x -> String.at(x, pos) end)
      |> Enum.filter(fn x -> x == "0" end)
      |> Enum.count()

    if zeroes * 2 > Enum.count(numbers) do
      "0"
    else
      "1"
    end
  end

  def getOxygen(numbers, pos \\ 0) do
    if Enum.count(numbers) == 1 do
      numbers
      |> Enum.at(0)
      |> String.to_integer(2)
    else
      bit = mostCommon(numbers, pos)
      Day3.getOxygen(Enum.filter(numbers, fn x -> String.at(x, pos) == bit end), pos + 1)
    end
  end

  def getCO2(numbers, pos \\ 0) do
    if Enum.count(numbers) == 1 do
      numbers
      |> Enum.at(0)
      |> String.to_integer(2)
    else
      bit = mostCommon(numbers, pos)
      Day3.getCO2(Enum.filter(numbers, fn x -> String.at(x, pos) != bit end), pos + 1)
    end
  end
end

{:ok, file} = File.read("inputs/day3.in")

numbers = String.split(file, "\n", trim: true)

most_frequent =
  0..(String.length(Enum.at(numbers, 0)) - 1)
  |> Enum.map(fn pos -> Day3.mostCommon(numbers, pos) end)

gamma =
  most_frequent
  |> Enum.join()
  |> String.to_integer(2)

epsilon =
  most_frequent
  |> Enum.map(fn x ->
    if x == "0" do
      "1"
    else
      "0"
    end
  end)
  |> Enum.join()
  |> String.to_integer(2)

IO.inspect(gamma * epsilon, label: "Part 1")

oxygen =
  Day3.getOxygen(numbers)
  |> IO.inspect(label: "oxygen")

co2 =
  Day3.getCO2(numbers)
  |> IO.inspect(label: "CO2")

IO.inspect(oxygen * co2, label: "Part 2")
