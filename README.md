# teams-league-python-ddd-beam-summit

## Run job with Dataflow runner :

```
python -m team_league.application.team_league_app \
    --project=emea-c1-dwh-dev \
    --project_id=emea-c1-dwh-dev \
    --job_name=team-league-python-job-$(date +'%Y-%m-%d-%H-%M-%S') \
    --runner=DataflowRunner \
    --staging_location=gs://mazlum_dev/dataflow/staging \
    --region=europe-west1 \
    --job_type=team_league_python_ingestion_job \
    --setup_file=./setup.py \
    --temp_location=gs://mazlum_dev/dataflow/temp \
    --team_league_dataset="mazlum_test" \
    --team_stats_table="team_stat" \
    --failure_output_dataset="mazlum_test" \
    --failure_output_table="job_failure" \
    --failure_feature_name="team_league"
```