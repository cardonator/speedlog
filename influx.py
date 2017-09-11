from influxdb import InfluxDBClient
import config

class InfluxLogger(object):
    influx_client = None

    def __init__(self):
        self.influx_client = InfluxDBClient(
            config.INFLUX_HOST,
            config.INFLUX_PORT,
            username=config.INFLUX_USER,
            password=config.INFLUX_PASS,
            database=config.INFLUX_DB,
            ssl=False,
            verify_ssl=False
        )

    def log(self, results):
        measurement = self.build_influx_measurement(results)
        self.influx_client.write_points(measurement)
        print measurement

    def build_influx_measurement(self, results):
        input_points = [
            {
                'measurement': 'speed_test_results',
                'fields': {
                    'download': results['download'],
                    'upload': results['upload'],
                    'ping': results['ping'],
                    "sponsor": results["sponsor"]
                },
                'tags': {
                    'server': "unset hostname"
                }
            }
        ]
        return input_points
