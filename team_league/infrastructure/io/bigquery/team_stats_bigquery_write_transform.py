import dataclasses
from typing import Dict

import apache_beam as beam
from apache_beam import PTransform
from apache_beam.pvalue import PCollection

from team_league.application.team_league_options import TeamLeagueNamesOptions
from team_league.domain.team_stats import TeamStats


class TeamStatsBigqueryWriteTransform(PTransform):

    def __init__(self,
                 pipeline_options: TeamLeagueNamesOptions):
        super().__init__()
        self.pipeline_options = pipeline_options

    def expand(self, teams_stats: PCollection[TeamStats]):
        return (teams_stats
                | 'Map to team stats bq dicts' >>
                beam.Map(self.to_team_stats_bq)
                | 'Write team stats to BQ' >> beam.io.WriteToBigQuery(
                    project=self.pipeline_options.project_id,
                    dataset=self.pipeline_options.team_league_dataset,
                    table=self.pipeline_options.team_stats_table,
                    write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                    create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER))

    def to_team_stats_bq(self, team_stats: TeamStats) -> Dict:
        return dataclasses.asdict(team_stats)
