x <- c(10,4,5.6, 3.1, 6.4, 21.7)
print(x[1])
print(x[3])
1/x
y <- c(x,0,x)
v<- 2*x +1 + y
r <- range(x)
mu <- mean(x)
sigma <- var(x)
y <-sort(x)
sort.list(x)
a <- 1:30
b <- 2*1:15
n <- 10
c <- 1:n-1
d <- 1:(n-1)
s3 <- seq(-5,5, by= 0.2)
s4 <- seq(length=51, from=-5, by=0.2)
s4 <- seq(from=-5, by=0.2, along = x) # same length as x
s5 <- rep(x, times=5)
s6 <- rep(x, each=5)
