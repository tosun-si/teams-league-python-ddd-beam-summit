from dependency_injector import containers, providers

from team_league.application.team_league_pipeline_composer import TeamLeaguePipelineComposer
from team_league.infrastructure.io.bigquery.team_stats_bigquery_io_adapter import TeamStatsBigqueryIOAdapter
from team_league.infrastructure.io.bigquery.team_stats_bigquery_write_transform import TeamStatsBigqueryWriteTransform
from team_league.infrastructure.io.jsonfile.team_stats_jsonfile_io_adapter import TeamStatsJsonFileIOAdapter
from team_league.infrastructure.io.jsonfile.team_stats_jsonfile_read_transform import TeamStatsJsonFileReadTransform
from team_league.infrastructure.io.mock.team_stats_mock_io_adapter import TeamStatsMockIOAdapter
from team_league.infrastructure.io.mock.team_stats_mock_read_transform import TeamStatsMockReadTransform
from team_league.infrastructure.io.pubsub.team_stats_pubsub_io_adapter import TeamStatsPubSubIOAdapter
from team_league.infrastructure.io.pubsub.team_stats_pubsub_read_transform import TeamStatsPubSubReadTransform


class Adapters(containers.DeclarativeContainer):
    pipeline_options = providers.Configuration()

    read_teams_stats_inmemory_transform = providers.Singleton(TeamStatsMockReadTransform)
    read_teams_stats_file_transform = providers.Singleton(TeamStatsJsonFileReadTransform,
                                                          pipeline_options=pipeline_options)
    read_teams_stats_topic_transform = providers.Singleton(TeamStatsPubSubReadTransform,
                                                           pipeline_options=pipeline_options)

    write_team_stats_database_transform = providers.Singleton(TeamStatsBigqueryWriteTransform,
                                                              pipeline_options=pipeline_options)

    team_stats_inmemory_io_connector = providers.Singleton(
        TeamStatsMockIOAdapter,
        read_transform=read_teams_stats_inmemory_transform)

    team_stats_file_io_connector = providers.Singleton(
        TeamStatsJsonFileIOAdapter,
        read_transform=read_teams_stats_file_transform)

    team_stats_topic_io_connector = providers.Singleton(
        TeamStatsPubSubIOAdapter,
        read_transform=read_teams_stats_topic_transform)

    team_stats_database_io_connector = providers.Singleton(
        TeamStatsBigqueryIOAdapter,
        write_transform=write_team_stats_database_transform)


class Pipeline(containers.DeclarativeContainer):
    pipeline_options = providers.Configuration()

    adapters = providers.DependenciesContainer()

    compose_pipeline = providers.Factory(
        TeamLeaguePipelineComposer,
        pipeline_options=pipeline_options,
        team_stats_inmemory_io_connector=adapters.team_stats_inmemory_io_connector,
        team_stats_database_io_connector=adapters.team_stats_database_io_connector,
        team_stats_file_io_connector=adapters.team_stats_file_io_connector,
        team_stats_topic_io_connector=adapters.team_stats_topic_io_connector
    )
