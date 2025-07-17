ts.sim <- arima.sim(list(order = c(1,1,0), ar = 0.7), n = 200)
ts.plot(ts.sim)
ts.sim2 <- arima.sim(n = 63, list(ar = c(0.8897, -0.4858), ma = c(-0.2279, 0.2488)), rand.gen = function(n, ...) sqrt(0.1796) * rt(n, df = 5))
ts.plot(ts.sim2)
## Generating AR and MA coefficients
x <- sample.int(10, 2, replace=TRUE) # p <- x[1], q <- x[2]
ar_coeffs <- runif(x[1],0,1) # ar is a array of size x[1] of coefficients between 0 and 1
ma_coeffs <- runif(x[2],0,1) # ma is a array of size x[2] of coefficients between 0 and 1
ts.sim3 <- arima.sim(n=200, list(ar = ar_coeffs, ma = ma_coeffs), rand.gen = function(n, ...) sqrt(0.1796) * rt(n, df = 5))
ts.plot(ts.sim3)
## Checking if the roots of the companion matrix for the ar_coeffs are outside the unit circle
roots_ar = polyroot(ar_coeffs) # roots of the companion matrix of the ar coefficients
## same thing with the ma_coeffs 