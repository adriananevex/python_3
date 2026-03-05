import sys

def main():
  print("=== Player Score Analytics ===")

  if len(sys.argv) == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    return

  scores = []

  for arg in sys.argv[1:]:
    try:
      score = int(arg)
      scores.append(score)
    except:
      print("Invalid score ignored:", arg)

  if len(scores) == 0:
    print("No valid numeric scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    return

  total_players = len(scores)
  total_score = sum(scores)
  avg_score = total_score / total_players
  high_score = max(scores)
  low_score = min(scores)
  score_range = high_score - low_score

  print("Scores processed:", scores)
  print("Total players:", total_players)
  print("Total score:", total_score)
  print("Average score:", avg_score)
  print("High score:", high_score)
  print("Score range:", score_range)

if __name__ == "__main__":
  main()
