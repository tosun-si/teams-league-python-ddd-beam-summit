import json
from typing import Dict

import apache_beam as beam
from apache_beam import PTransform
from apache_beam.io import ReadFromPubSub
from apache_beam.pvalue import PBegin
from dacite import from_dict

from team_league.application.pipeline_conf import PipelineConf
from team_league.domain.team_stats_raw import TeamStatsRaw


class TeamStatsPubSubReadTransform(PTransform):

    def __init__(self,
                 pipeline_conf: PipelineConf):
        super().__init__()
        self.pipeline_conf = pipeline_conf

    def expand(self, inputs: PBegin):
        return (inputs |
                'Read team stats from pub sub' >> ReadFromPubSub(
                    subscription=self.pipeline_conf.input_subscription) |
                'Map bytes message to Dict' >> beam.Map(self.to_dict) |
                'Deserialize Dict to domain dataclass' >> beam.Map(self.deserialize))

    def to_dict(self, team_stats_raw: bytes) -> Dict:
        return json.loads(team_stats_raw.decode('utf-8'))

    def deserialize(self, team_stats_raw_as_dict: Dict) -> TeamStatsRaw:
        return from_dict(
            data_class=TeamStatsRaw,
            data=team_stats_raw_as_dict
        )
