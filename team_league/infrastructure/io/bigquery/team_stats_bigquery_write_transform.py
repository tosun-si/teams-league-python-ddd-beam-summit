import dataclasses
from datetime import datetime
from typing import Dict

import apache_beam as beam
from apache_beam import PTransform
from apache_beam.pvalue import PCollection

from team_league.application.pipeline_conf import PipelineConf
from team_league.domain.team_stats import TeamStats


class TeamStatsBigqueryWriteTransform(PTransform):

    def __init__(self,
                 pipeline_conf: PipelineConf):
        super().__init__()
        self.pipeline_conf = pipeline_conf

    def expand(self, teams_stats: PCollection[TeamStats]):
        return (teams_stats
                | 'Map to team stats bq dicts' >>
                beam.Map(self.to_team_stats_bq)
                | 'Write team stats to BQ' >> beam.io.WriteToBigQuery(
                    project=self.pipeline_conf.project_id,
                    dataset=self.pipeline_conf.team_league_dataset,
                    table=self.pipeline_conf.team_stats_table,
                    method=self.pipeline_conf.bq_write_method,
                    write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                    create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER))

    def to_team_stats_bq(self, team_stats: TeamStats) -> Dict:
        team_stats_as_dict = dataclasses.asdict(team_stats)
        team_stats_as_dict.update({'ingestionDate': datetime.utcnow().isoformat()})

        return team_stats_as_dict
