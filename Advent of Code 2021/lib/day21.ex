defmodule Day21 do
  def roll(prev_result) do
    if prev_result == 100 do
      1
    else
      prev_result + 1
    end
  end

  def roll3(prev_result) do
    a = Day21.roll(prev_result)
    b = Day21.roll(a)
    c = Day21.roll(b)
    [a + b + c, c]
  end

  def move(pos, score, prev_result) do
    [distance, last_result] = Day21.roll3(prev_result)
    new_pos = rem(pos + distance, 10)
    new_score = score + new_pos + 1
    [new_pos, new_score, last_result]
  end

  def play(pos1, pos2, score1 \\ 0, score2 \\ 0, prev_result \\ 100, n_rolls \\ 0) do
    [new_pos1, new_score1, last_result] = move(pos1, score1, prev_result)

    if new_score1 >= 1000 do
      score2 * (n_rolls + 3)
    else
      [new_pos2, new_score2, last_result] = move(pos2, score2, last_result)

      if new_score2 >= 1000 do
        score1 * (n_rolls + 6)
      else
        play(new_pos1, new_pos2, new_score1, new_score2, last_result, n_rolls + 6)
      end
    end
  end

  def play_part2(pos1, pos2, score1 \\ 0, score2 \\ 0, player \\ 0, universes \\ 1) do
    if player == 0 do
      # there are 27 possible roll outcomes, map result => frequency
      %{3 => 1, 4 => 3, 5 => 6, 6 => 7, 7 => 6, 8 => 3, 9 => 1}
      |> Enum.map(fn {distance, frequency} ->
        new_pos1 = rem(pos1 + distance, 10)
        new_score1 = score1 + new_pos1 + 1

        if new_score1 >= 21 do
          [frequency * universes, 0]
        else
          play_part2(new_pos1, pos2, new_score1, score2, 1, frequency * universes)
        end
      end)
      |> Enum.reduce(fn [a, b], [acc_a, acc_b] -> [a + acc_a, b + acc_b] end)
    else
      %{3 => 1, 4 => 3, 5 => 6, 6 => 7, 7 => 6, 8 => 3, 9 => 1}
      |> Enum.map(fn {distance, frequency} ->
        new_pos2 = rem(pos2 + distance, 10)
        new_score2 = score2 + new_pos2 + 1

        if new_score2 >= 21 do
          [0, frequency * universes]
        else
          play_part2(pos1, new_pos2, score1, new_score2, 0, frequency * universes)
        end
      end)
      |> Enum.reduce(fn [a, b], [acc_a, acc_b] -> [a + acc_a, b + acc_b] end)
    end
  end
end

'''
Player 1 starting position: 7
Player 2 starting position: 4
'''

Day21.play(6, 3)
|> IO.inspect(label: "Part 1")

Day21.play_part2(6, 3)
|> Enum.max()
|> IO.inspect(label: "Part 2")
