defmodule Day4 do
  @doc """
  process numbers until board wins or numbers run out
  returns {final_turn, score}
  """
  def board_score(board, numbers, turn \\ 0) do
    if turn >= Enum.count(numbers) do
      {turn, 0}
    else
      # mark numbers
      new_board =
        board
        |> Enum.map(fn x ->
          if x == Enum.at(numbers, turn) do
            "*"
          else
            x
          end
        end)

      if has_won(new_board) do
        {turn, score(new_board) * String.to_integer(Enum.at(numbers, turn))}
      else
        Day4.board_score(new_board, numbers, turn + 1)
      end
    end
  end

  def has_won(board) do
    # check rows
    if Enum.chunk_every(board, 5)
       |> Enum.filter(fn x -> Enum.all?(x, fn y -> y == "*" end) end)
       |> Enum.empty?() do
      if 0..4
         |> Enum.map(fn x ->
           board
           |> Enum.slice(x..25)
           |> Enum.take_every(5)
         end)
         |> Enum.filter(fn x -> Enum.all?(x, fn y -> y == "*" end) end)
         |> Enum.empty?() do
        false
      else
        true
      end
    else
      true
    end
  end

  def score(board) do
    board
    |> Enum.filter(fn x -> x != "*" end)
    |> Enum.map(&String.to_integer/1)
    |> Enum.sum()
  end
end

{:ok, file} = File.read("inputs/day4.in")

{numbers, boards} =
  file
  |> String.split("\n\n", trim: true)
  |> Enum.split(1)

numbers =
  numbers
  |> Enum.at(0)
  |> String.split(",")

boards =
  boards
  |> Enum.map(&String.split/1)

boards
|> Enum.map(fn board -> Day4.board_score(board, numbers) end)
|> Enum.sort()
|> Enum.at(0)
|> elem(1)
|> IO.inspect(label: "Part 1")

boards
|> Enum.map(fn board -> Day4.board_score(board, numbers) end)
|> Enum.sort()
|> Enum.at(-1)
|> elem(1)
|> IO.inspect(label: "Part 2")
