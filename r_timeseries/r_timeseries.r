# Description: Load daily time series and do prediction

# kings <- scan("http://robjhyndman.com/tsdldata/misc/kings.dat",skip=3)
# kings
# kingstimeseries <- ts(kings, start=c(1500))
# plot.ts(kingstimeseries)

# From https://stat.ethz.ch/R-manual/R-devel/library/stats/html/ts.html
# require(graphics)
# 
# ts(1:10, frequency = 4, start = c(1959, 2)) # 2nd Quarter of 1959
# print( ts(1:10, frequency = 7, start = c(12, 2)), calendar = TRUE)
# # print.ts(.)
# ## Using July 1954 as start date:
# gnp <- ts(cumsum(1 + round(rnorm(100), 2)),
#           start = c(1954, 7), frequency = 12)
# plot(gnp) # using 'plot.ts' for time-series plot

library("forecast")
data <- scan("/home/anthony/workspace/datascience/r_timeseries/data_pv.txt")
data_ts <- ts(data, freq=7, start=c(1,1))
plot.ts(data_ts)
data_forecast <- HoltWinters(data_ts)
data_forecast
plot(data_forecast)

data_forecast2 <- forecast.HoltWinters(data_forecast, h=365)
plot.forecast(data_forecast2)
