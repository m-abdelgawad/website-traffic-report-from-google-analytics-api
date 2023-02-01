import os
import yaml
import traceback
from packages.file import file
from packages.logger import logger
from packages.dateTimeTools import dateTimeTools
from packages.googleAnalytics import googleAnalytics

# https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#dimensions

# Initiate logger
log = logger.get(app_name='google-analytics')


def main():

    log.info('Start program execution')

    project_abs_path = file.caller_dir_path()

    # Import configurations
    config_path = os.path.join(project_abs_path, 'config.yaml')
    with open(config_path) as config_file:
        config = yaml.safe_load(config_file)

    # Set the dates dictionary
    start_date = dateTimeTools.get_past_date(
        days_count=30, output_format='%Y-%m-%d'
    )
    log.info('Start date: {0}'.format(start_date))

    end_date = dateTimeTools.get_today_date(output_format='%Y-%m-%d')
    log.info('End date: {0}'.format(end_date))
    dates_dict = {
        'start': start_date,
        'end': end_date,
    }

    # Get the key
    sa_key_path = os.path.join(
        project_abs_path, config['AnalyticsAccount']['key_path']
    )

    # Get the report response
    response = googleAnalytics.get_report(
        property_id=config['AnalyticsAccount']['property_id'],
        key_path=sa_key_path,
        dimensions_names=config['AnalyticsReport']['dimensions_names'],
        metrics_names=config['AnalyticsReport']['metrics'],
        dates_dict=dates_dict
    )

    # Initiate analytics variables
    total_users = 0
    users_dict = {}  # Time and users
    countries_dict = {}  # countries and users
    pagetitle_dict = {}  # Page title and users
    devices_dict = {}  # devices and users

    # Fetch Results
    for index, report in enumerate(response.reports):

        for row in report.rows:

            current_country = row.dimension_values[0].value
            current_date = row.dimension_values[1].value
            current_pagetitle = row.dimension_values[2].value
            current_device = row.dimension_values[3].value
            current_users_count = int(row.metric_values[0].value)

            total_users += current_users_count

            if current_date in users_dict:
                users_dict[current_date] += current_users_count
            else:
                users_dict[current_date] = current_users_count

            if current_country in countries_dict:
                countries_dict[current_country] += current_users_count
            else:
                countries_dict[current_country] = current_users_count

            if current_pagetitle in pagetitle_dict:
                pagetitle_dict[current_pagetitle] += current_users_count
            else:
                pagetitle_dict[current_pagetitle] = current_users_count

            if current_device in devices_dict:
                devices_dict[current_device] += current_users_count
            else:
                devices_dict[current_device] = current_users_count

    # Get the labels and data of the users per time graph
    users_time_dict = {}
    users_time_labels = []
    users_time_data = []
    for date in users_dict:
        date_formatted = dateTimeTools.reformat_date(
            input_date=date,
            current_format='%Y%m%d',
            target_format='%Y-%m-%d'
        )
        users_time_labels.append(date_formatted)
        users_time_data.append(users_dict[date])
    # Get the labels and data of the users per country graph
    users_country_labels = [key for key in countries_dict]
    users_country_data = [countries_dict[key] for key in users_country_labels]

    # Get the labels and data of the users per PageTitle graph
    # Remote the website part from the title, for example:
    # 'Contact - Automagic Developer' ---> 'Contact'
    users_page_labels = [key.split(' -')[0] for key in pagetitle_dict]
    users_page_data = [pagetitle_dict[key] for key in pagetitle_dict]

    # Get the labels and data of the users per device graph
    users_device_labels = [key for key in devices_dict]
    users_device_data = [devices_dict[key] for key in users_device_labels]

    log.info('Total users: {0:,d}\n'.format(total_users))

    log.info('Users per Time dict: {0}'.format(users_dict))
    log.info('Users per Time labels: {0}'.format(users_time_labels))
    log.info('Users per Time data: {0}\n'.format(users_time_data))

    log.info('Users per Country dict: {0}'.format(countries_dict))
    log.info('Users per Country labels: {0}'.format(users_country_labels))
    log.info('Users per Country data: {0}\n'.format(users_country_data))

    log.info('Users per PageTitle dict: {0}'.format(pagetitle_dict))
    log.info('Users per PageTitle labels: {0}'.format(users_page_labels))
    log.info('Users per PageTitle data: {0}\n'.format(users_page_data))

    log.info('Users per Devices dict: {0}'.format(devices_dict))
    log.info('Users per Device labels: {0}'.format(users_device_labels))
    log.info('Users per Device data: {0}\n'.format(users_device_data))

    output_dict = {
        'start_date': start_date,
        'end_date': end_date,
        'total_users': total_users,
        'users_time_labels': users_time_labels,
        'users_time_data': users_time_data,
        'users_country_labels': users_country_labels,
        'users_country_data': users_country_data,
        'users_page_labels': users_page_labels,
        'users_page_data': users_page_data,
        'users_device_labels': users_device_labels,
        'users_device_data': users_device_data,
    }

    log.info('Finished program execution')

    return output_dict


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        log.error(e)
        log.error('Error Traceback: \n {0}'.format(traceback.format_exc()))
