from apache_beam import PTransform

from team_league.domain_ptransform.team_stats_topic_io_connector import TeamStatsTopicIOConnector
from team_league.infrastructure.io.pubsub.team_stats_pubsub_read_transform import TeamStatsPubSubReadTransform


class TeamStatsPubSubIOAdapter(TeamStatsTopicIOConnector):

    def __init__(self,
                 read_transform: TeamStatsPubSubReadTransform) -> None:
        super().__init__()
        self.read_transform = read_transform

    def read_team_stats(self) -> PTransform:
        return self.read_transform
