import speedtest
import arrow


class SpeedTestLog(object):
    results = {
        "download": None,
        "upload": None,
        "ping": None,
        "timestamp": None,
        "sponsor": None,
        "server": None,
    }

    def execute(self):
        """ runs the actual speed test """
        tester = speedtest.Speedtest()
        tester.get_best_server()
        tester.download()
        tester.upload()
        self.parse_results(tester.results)

    def parse_results(self, results):
        """ returns speeds in mbps """
        self.results["download"] = round(results.download / 1000000, 1)
        self.results["upload"] = round(results.upload / 1000000, 1)
        self.results["ping"] = results.ping
        self.results["timestamp"] = arrow.get(results.timestamp).datetime
        self.results["sponsor"] = results.server["sponsor"]
        self.results["server"] = "speedtest"

    def get_results(self):
        """ returns the results """
        return self.results
