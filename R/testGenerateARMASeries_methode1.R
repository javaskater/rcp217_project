


check_stationarity_of_coefficients <- function(coeffs) {
  roots = polyroot(coeffs)
  is_stationary <- TRUE
  for (root_value in roots){
    if (Mod(root_value) <= 1.1){ 
        string_to_print <- sprintf("[check_stationarity_of_coefficients] For the complex roof %f+%fi the norm id %f is below 1", Re(root_value), Im(root_value), Mod(root_value))
        print(string_to_print)
        is_stationary <- FALSE
        break
    }
  }
  return (is_stationary)
}

# the order parameter is the number 
## p of ar coefficients 
## or q of ma coefficients
# It returns le vector of the p respective q coefficients that make it stationary
calculate_stationary_coefficients <- function(order){
    stationarity_check <- FALSE
    coeffs <- c()
    # https://www.w3schools.com/r/r_while_loop.asp the while loop in R
    while(! stationarity_check){
        coeffs <- runif(order,0,1) # generates order number of coeffcients between 0 and 1
        stationarity_check <- check_stationarity_of_coefficients(coeffs)
    }
    string_to_print <- sprintf("[calculate_stationary_coefficients] stationary coefficients found %s",  paste0(coeffs, collapse = "|"))
    print(string_to_print)
    roots = polyroot(coeffs)
    for (root_value in roots){
      string_to_print <- sprintf("[calculate_stationary_coefficients] ++ root found %f+%f i module %f", Re(root_value), Im(root_value),  Mod(root_value))
      print(string_to_print)
    }
    return (coeffs)
}

# test with a 4 for ar
ar_coeffs <- calculate_stationary_coefficients(4)
# test a  ar1 <- arima.sim(model = list(order = c(4,0,0), ar = ar_coeffs), n = 200)
ar1 <- arima.sim(model = list(order = c(4,0,0), ar = ar_coeffs), n = 200)
# followed by ts.plot(ar1)