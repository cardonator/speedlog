import fast_com
import arrow


class FastLog(object):
    results = {
        "download": None,
        "upload": None,
        "ping": None,
        "timestamp": None,
        "sponsor": None,
    }

    def execute(self):
        """ run the actual speed test """
        result = fast_com.fast_com()
        self.parse_results(result)

    def parse_results(self, results):
        """ parse the results into something parseable for the logger """
        self.results["download"] = results
        self.results["timestamp"] = arrow.utcnow().datetime
        self.results["sponsor"] = "netflix"
        self.results["server"] = "netflix"

    def get_results(self):
        """ return the results """
        return self.results
