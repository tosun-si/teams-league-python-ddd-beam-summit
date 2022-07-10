from apache_beam import PTransform

from team_league.domain_transform.team_stats_inmemory_io_connector import TeamStatsInMemoryIOConnector
from team_league.infrastructure.io.mock.team_stats_mock_read_transform import TeamStatsMockReadTransform


class TeamStatsMockIOAdapter(TeamStatsInMemoryIOConnector):

    def __init__(self,
                 read_transform: TeamStatsMockReadTransform) -> None:
        super().__init__()
        self.read_transform = read_transform

    def read_team_stats(self) -> PTransform:
        return self.read_transform
