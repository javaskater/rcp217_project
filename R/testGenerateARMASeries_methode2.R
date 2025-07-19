calculate_times_serie <- function(p, q){
  stationary_time_serie <- FALSE
  time_serie <- c()
  ar_coeffs <- c()
  ma_coeffs <- c()
  while (!stationary_time_serie){
    tryCatch(                
      expr = { 
        ar_coeffs <- runif(p,0,1) # generates order number of coeffcients between 0 and 1
        ma_coeffs <- runif(q,0,1) # generates order number of coeffcients between 0 and 1
        msg_str = sprintf("[calculate_times_serie] checking ar_coeffs: %s with ma_coeffs: %s", paste0(ar_coeffs, collapse = "|"), paste0(ma_coeffs, collapse = "|"))
        print(msg_str)
        #time_serie <<- arima.sim(model = list(order = c(p,0,q), ar = ar_coeffs, ma = ma_coeffs), n = 200)
        time_serie <- arima.sim(model = list(ar = ar_coeffs, ma = ma_coeffs), n = 200)
        # if we pass the previous expression we have a stationary time serie
        stationary_time_serie <<- TRUE
        msg_str = sprintf("[calculate_times_serie] Everything was fine. the serie is stationary")
        print(msg_str)
        break
      },
      error = function(e){
        stationary_time_serie <<- FALSE
        msg_str = sprintf("[calculate_times_serie] error ar ma coefficients not stationary. Message d'erreur:%s", e$message)
        print(msg_str)
      },
      
      warning = function(w){       
        stationary_time_serie <<- FALSE
        msg_str = sprintf("[calculate_times_serie] Message de warning %s", w$message)
        print(msg_str)
      },
      
      finally = {             
        print("[calculate_times_serie] + finally Executed")
      }
    )
  }
  return (list(ar_coefficients <- ar_coeffs, ma_coefficients <- ma_coeffs, arma_timeserie <- time_serie))
}

my_ts <- calculate_times_serie(4,5)
arma1 = my_ts[[3]]
ts.plot(arma1)
