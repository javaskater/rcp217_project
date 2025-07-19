
stationary_time_serie <- True
tryCatch(                
  expr = {                      
    ts.sim4 <- arima.sim(n=200, list(ar = ar_coeffs, ma = ma_coeffs), rand.gen = function(n, ...) sqrt(0.1796) * rt(n, df = 5))
    ar1 <- arima.sim(model = list(order = c(4,0,0), ar = ar_coeffs), n = 200)
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
# test a  ar1 <- arima.sim(model = list(order = c(4,0,0), ar = ar_coeffs), n = 200)
ar1 <- arima.sim(model = list(order = c(4,0,0), ar = ar_coeffs), n = 200)
# followed by ts.plot(ar1)