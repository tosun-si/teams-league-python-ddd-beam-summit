from dataclasses import dataclass


@dataclass
class PipelineConf:
    project_id: str
    input_json_file: str
    input_subscription: str
    team_league_dataset: str
    team_stats_table: str
    bq_write_method: str

    @staticmethod
    def to_pipeline_conf(option):
        return PipelineConf(
            project_id=option.project_id,
            input_json_file=option.input_json_file,
            input_subscription=option.input_subscription,
            team_league_dataset=option.team_league_dataset,
            team_stats_table=option.team_stats_table,
            bq_write_method=option.bq_write_method
        )
