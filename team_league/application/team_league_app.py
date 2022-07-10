import logging

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

from team_league.application.team_league_options import TeamLeagueNamesOptions
from team_league.injection.containers import Adapters, Pipeline


def main() -> None:
    logging.getLogger().setLevel(logging.INFO)

    team_league_options = PipelineOptions().view_as(TeamLeagueNamesOptions)
    pipeline_options = PipelineOptions()

    with beam.Pipeline(options=pipeline_options) as p:
        adapters = Adapters(pipeline_options=team_league_options)
        pipeline = Pipeline(pipeline_options=team_league_options, adapters=adapters)

        pipeline_composer = pipeline.compose_pipeline()
        pipeline_composer.compose(pipeline=p)


if __name__ == "__main__":
    main()
