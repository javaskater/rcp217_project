calculate_times_serie <- function(p, q, ts_length = 200){
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

generate_time_serie_in_csv <- function(p,q,  ts_length = 200){
  timestamp_generation_serie <- format(Sys.time(), format="%d%m%Y%H%M%S")
  ts_file_name <- sprintf("ar_%d__ma_%d__time_%s.csv",p,q,timestamp_generation_serie)
  my_ts <- calculate_times_serie(p,q, ts_length)
  arma1 = my_ts[[3]]
  #ts.plot(arma1)
  # write.table(t(arma1), file="C:/Images/test.csv", sep=";") # on windows
  write.table(t(arma1), file = ts_file_name, fileEncoding = "UTF-8", sep=";") # t(arma1): t stands for transpose
}

mainDir <- "~/CONSULTANT"
#mainDir="C:/Images"
subDir <- sprintf("ts_generees_%s",format(Sys.Date(), format = "%d%m%Y"))
dir.create(file.path(mainDir, subDir), showWarnings = FALSE)
setwd(file.path(mainDir, subDir))
print(sprintf("[main] on va générer des times series en maase dans le répertoire %s/%s", mainDir, subDir))
time_serie_length <- 1000
numeric_range <- 0:9
for (p in numeric_range){
  for (q in numeric_range){
    print(sprintf("[main] on génère une time serie de %d données avec les coefficients AR: %d et MA: %d", time_serie_length, p, q))
    generate_time_serie_in_csv(p,q, time_serie_length)
  }
}

  
