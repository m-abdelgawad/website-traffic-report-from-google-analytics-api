import os
import logging
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
    BatchRunReportsRequest,
)


# Import logger
log = logging.getLogger(__name__)


def get_report(
        property_id, key_path, dimensions_names, metrics_names, dates_dict
):
    """
    Runs a batch report on a Google Analytics 4 property.
    Using a default constructor instructs the client to use the credentials
    specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
    """

    log.info('Start get_report function')

    # Set environment variables
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path

    client = BetaAnalyticsDataClient()

    dimensions_list = []
    for dimension_name in dimensions_names:
        dimensions_list.append(Dimension(name=dimension_name))

    metrics_list = []
    for metric_name in metrics_names:
        metrics_list.append(Metric(name=metric_name))

    requests = BatchRunReportsRequest(
        property=f"properties/{property_id}",
        requests=[
            RunReportRequest(
                dimensions=dimensions_list,
                metrics=metrics_list,
                date_ranges=[
                    DateRange(
                        start_date=dates_dict['start'],
                        end_date=dates_dict['end']
                    )
                ]
            )
        ]
    )
    response = client.batch_run_reports(requests)

    log.info('Finished get_report function')

    return response
