# teams-league-python-ddd-beam-summit

## Run job with Dataflow runner :

### Batch

```
python -m team_league.application.team_league_app \
    --project=emea-c1-dwh-dev \
    --project_id=emea-c1-dwh-dev \
    --streaming=false \
    --input_json_file=gs://mazlum_dev/team_league/input/json/input_teams_stats_raw.json \
    --job_name=team-league-python-job-$(date +'%Y-%m-%d-%H-%M-%S') \
    --runner=DataflowRunner \
    --staging_location=gs://mazlum_dev/dataflow/staging \
    --region=europe-west1 \
    --setup_file=./setup.py \
    --temp_location=gs://mazlum_dev/dataflow/temp \
    --team_league_dataset="mazlum_test" \
    --team_stats_table="team_stat" \
    --bq_write_method=FILE_LOADS \
```

### Streaming

```
python -m team_league.application.team_league_app \
    --project=emea-c1-dwh-dev \
    --project_id=emea-c1-dwh-dev \
    --streaming=true \
    --input_json_file=gs://mazlum_dev/team_league/input/json/input_teams_stats_raw.json \
    --input_subscription=projects/emea-c1-dwh-dev/subscriptions/team_league \
    --job_name=team-league-python-job-$(date +'%Y-%m-%d-%H-%M-%S') \
    --runner=DataflowRunner \
    --staging_location=gs://mazlum_dev/dataflow/staging \
    --region=europe-west1 \
    --setup_file=./setup.py \
    --temp_location=gs://mazlum_dev/dataflow/temp \
    --team_league_dataset="mazlum_test" \
    --team_stats_table="team_stat" \
    --bq_write_method=STREAMING_INSERTS \
```