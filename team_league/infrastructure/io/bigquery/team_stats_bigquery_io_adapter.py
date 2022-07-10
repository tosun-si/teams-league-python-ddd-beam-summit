from apache_beam import PTransform

from team_league.domain_transform.team_stats_database_io_connector import TeamStatsDatabaseIOConnector
from team_league.infrastructure.io.bigquery.team_stats_bigquery_write_transform import TeamStatsBigqueryWriteTransform


class TeamStatsBigqueryIOAdapter(TeamStatsDatabaseIOConnector):

    def __init__(self,
                 write_transform: TeamStatsBigqueryWriteTransform) -> None:
        super().__init__()
        self.write_transform = write_transform

    def write_team_stats(self) -> PTransform:
        return self.write_transform
