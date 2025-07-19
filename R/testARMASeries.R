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
## check if the root of the  
for (ar_value in roots_ar){
  string_to_print <- sprintf("For the complex roof %f+%fi the norm id %f", Re(ar_value), Im(ar_value), Mod(ar_value))
  print(string_to_print)
}
## check root with the ma_coeffs 
roots_ma = polyroot(ma_coeffs) # roots of the companion matrix of the ar coefficients
## check if the root of the  ma coefficients compnion matrix are inside the circle
for (ma_value in roots_ma){
  string_to_print <- sprintf("For the complex roof %f+%fi the norm id %f", Re(ma_value), Im(ma_value), Mod(ma_value))
  print(string_to_print)
}
# No need to check the roots of the Companion Matrix arima.sim check itself if if the ar or ma part of the coefficient is stationary 
stationary_time_serie <- TRUE
tryCatch(                
  expr = {                      
    ts.sim4 <- arima.sim(n=200, list(ar = ar_coeffs, ma = ma_coeffs), rand.gen = function(n, ...) sqrt(0.1796) * rt(n, df = 5))
    stationary_time_serie <- TRUE
    print("Everything was fine. the serie is stationary I Plot")
    ts.plot(ts.sim4)
  },
  error = function(e){
    stationary_time_serie <<- FALSE
    message("There was an error message.", e)
  },
  
  warning = function(w){       
    stationary_time_serie <<- FALSE
    message("There was a warning message.", w)
  },
  
  finally = {             
    print("finally Executed")
  }
)
if (stationary_time_serie) {
  print(sprintf("[main] Everything was OK I already plotted"))
}
# calling arima.sim 2 times with only the p d q orders and letting arima.sim finding coefficients that make the model stationary
## generating the orders randomly etween 1 and 10
x <- sample.int(10, 2, replace=TRUE) # p <- x[1], q <- x[2]
p <- x[1]
q <- x[2]
ts.sim10 <- arima.sim(n=200, model = list(order = c(p,0,q)), rand.gen = function(n, ...) sqrt(0.1796) * rt(n, df = 5)) # does not work
ts.plot(ts.sim10)
x <- sample.int(10, 2, replace=TRUE) # p <- x[1], q <- x[2]
p <- x[1]
q <- x[2]
ts.sim11 <- arima.sim(n=200, model = list(order = c(p,0,q)), rand.gen = function(n, ...) sqrt(0.1796) * rt(n, df = 5)) # does not work
ts.plot(ts.sim11)