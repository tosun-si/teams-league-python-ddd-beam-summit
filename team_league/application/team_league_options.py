from apache_beam.options.pipeline_options import PipelineOptions


class TeamLeagueNamesOptions(PipelineOptions):

    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument("--project_id", help="GCP Project ID", required=True)
        parser.add_argument("--team_league_dataset", help="Team league dataset", required=True)
        parser.add_argument("--team_stats_table", help="Team stats table", required=True)
        parser.add_argument("--job_type", help="Current job type", required=True)
        parser.add_argument("--failure_output_dataset", help="Output dataset for failures", required=True)
        parser.add_argument("--failure_output_table", help="Output table for failures", required=True)
        parser.add_argument("--failure_feature_name", help="Feature name for failures", required=True)
