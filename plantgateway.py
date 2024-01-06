#!/usr/bin/python3
##############################################
#
# This is open source software licensed under the Apache License 2.0
# http://www.apache.org/licenses/LICENSE-2.0
#
##############################################

from plantgw.plantgw import PlantGateway, SensorConfig
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Collect data from Mi Flora plant sensors")
    parser.add_argument('-c', '--config', type=str, default='~/.plantgw.yaml', help="Path to the configuration file")
    args = parser.parse_args()

    config_file_path = args.config
    pg = PlantGateway(config_file_path)
    failed_sensors = pg.process_all()
    if len(failed_sensors) > 0:
        print('Could not get data from {}sensor(s): {}.'.format(
            len(failed_sensors),
            SensorConfig.get_name_string(failed_sensors)))
    pg.stop_client()
    # only count the sensors that are NOT fail silent
    num_failed = len([s for s in failed_sensors if not s.fail_silent])
    sys.exit(num_failed)


if __name__ == '__main__':
    main()
