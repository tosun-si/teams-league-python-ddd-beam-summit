from abc import ABCMeta, abstractmethod

from apache_beam import Pipeline

from team_league.application.pipeline_conf import PipelineConf
from team_league.domain_ptransform.team_stats_database_io_connector import TeamStatsDatabaseIOConnector
from team_league.domain_ptransform.team_stats_file_io_connector import TeamStatsFileIOConnector
from team_league.domain_ptransform.team_stats_inmemory_io_connector import TeamStatsInMemoryIOConnector
from team_league.domain_ptransform.team_stats_topic_io_connector import TeamStatsTopicIOConnector
from team_league.domain_ptransform.team_stats_transform import TeamStatsTransform


class PipelineComposer(metaclass=ABCMeta):

    @abstractmethod
    def compose(self) -> Pipeline:
        pass


class TeamLeaguePipelineComposer:

    def __init__(self,
                 pipeline_conf: PipelineConf,
                 team_stats_inmemory_io_connector: TeamStatsInMemoryIOConnector,
                 team_stats_database_io_connector: TeamStatsDatabaseIOConnector,
                 team_stats_file_io_connector: TeamStatsFileIOConnector,
                 team_stats_topic_io_connector: TeamStatsTopicIOConnector) -> None:
        super().__init__()
        self.pipeline_conf = pipeline_conf
        self.team_stats_inmemory_io_connector = team_stats_inmemory_io_connector
        self.team_stats_database_io_connector = team_stats_database_io_connector
        self.team_stats_file_io_connector = team_stats_file_io_connector
        self.team_stats_topic_io_connector = team_stats_topic_io_connector

    def compose(self, pipeline: Pipeline) -> Pipeline:
        (pipeline
         | 'Read team stats' >> self.team_stats_topic_io_connector.read_team_stats()
         | 'Team stats domain transform' >> TeamStatsTransform()
         | 'Write team stats to db' >> self.team_stats_database_io_connector.write_team_stats())

        return pipeline
