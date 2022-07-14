import logging

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

from team_league.application.pipeline_conf import PipelineConf
from team_league.application.team_league_options import TeamLeagueOptions
from team_league.injection.containers import Adapters, Pipeline, IOTransforms


def main() -> None:
    logging.getLogger().setLevel(logging.INFO)

    team_league_options = PipelineOptions().view_as(TeamLeagueOptions)
    pipeline_options = PipelineOptions()
    pipeline_config = PipelineConf.to_pipeline_conf(team_league_options)

    with beam.Pipeline(options=pipeline_options) as p:
        io_transforms = IOTransforms(config=pipeline_config)

        adapters = Adapters(io_transforms=io_transforms)
        pipeline = Pipeline(config=pipeline_config, adapters=adapters)

        pipeline_composer = pipeline.compose_pipeline()
        pipeline_composer.compose(pipeline=p)


if __name__ == "__main__":
    main()
