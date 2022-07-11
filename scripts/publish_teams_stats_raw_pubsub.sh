while read team_stat_message; do
  echo "Publishing team stats raw message $team_stat_message"

  gcloud pubsub topics publish team_league \
    --message="$team_stat_message"

done <input_teams_stats_raw_pubsub.json

