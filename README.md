# SpeedLog

SpeedLog is a python app for running internet speed tests and injecting them into a time series or log aggregation framework.

Currently, only `Speedtest.net` and `fast.com` are supported, however SpeedLog is designed to be a lightweight middleman between implementations of testers and loggers. In theory it could be used to run any kind of test and post its results to any aggregator.

On the log side, only `InfluxDB` is supported right now because it is really excellent at time series.

# Usage

## Simple Example

To run your first test, you can set your influx server atributes in a config.py and then simply run

```
python speedlog.py
```

By default, speedlog runs both speedtest and fast.com tests and sticks them in influx.    

## Using python

You can also call into speedlog from python.

```
SpeedLog(["speedtestlog.SpeedTestLog", "fastlog.FastLog"], ["influx.InfluxLogger"]).execute()
```
or
```
speedlog = SpeedLog()
speedlog.register_tester("speedtestlog.SpeedTestLog")
speedlog.register_tester("fastlog.FastLog")
speedlog.register_logger("influx.InfluxLogger")
speedlog.execute()
```