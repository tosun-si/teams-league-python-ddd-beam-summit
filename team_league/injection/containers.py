from dependency_injector import containers, providers

from team_league.application.team_league_pipeline_composer import TeamLeaguePipelineComposer
from team_league.infrastructure.io.bigquery.team_stats_bigquery_io_adapter import TeamStatsBigqueryIOAdapter
from team_league.infrastructure.io.bigquery.team_stats_bigquery_write_transform import TeamStatsBigqueryWriteTransform
from team_league.infrastructure.io.mock.team_stats_mock_io_adapter import TeamStatsMockIOAdapter
from team_league.infrastructure.io.mock.team_stats_mock_read_transform import TeamStatsMockReadTransform


class Adapters(containers.DeclarativeContainer):
    pipeline_options = providers.Configuration()

    read_teams_stats_inmemory_transform = providers.Singleton(TeamStatsMockReadTransform)
    write_team_stats_database_transform = providers.Singleton(TeamStatsBigqueryWriteTransform,
                                                              pipeline_options=pipeline_options)

    team_stats_inmemory_io_connector = providers.Singleton(
        TeamStatsMockIOAdapter,
        read_transform=read_teams_stats_inmemory_transform)

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
        team_stats_database_io_connector=adapters.team_stats_database_io_connector
    )
