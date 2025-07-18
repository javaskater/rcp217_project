# Références
[Journal of Statistical Software](https://www.jstatsoft.org/article/view/v027i03)
* utilisant la même méthode arima dans [cet article](https://www.numberanalytics.com/blog/arma-models-time-series-analysis)
* le code [R simule une time serie](https://rdrr.io/r/stats/arima.sim.html)
* nous demande que les coefficients aient de racines 1 1.001 pour stabilité
* un exemple [simulation](https://kevinkotze.github.io/ts-2-tut/)
# Code
## tests unitaires sous [tests avec aima.sim](../../R/testARMASeries.R)
* je suis bloqué à calculer les racines des Companion Matrices (des Imaginaires)
* Il faut [installer](https://dh-r.lincolnmullen.com/installing-r-and-packages.html) le [polyroot package](https://search.r-project.org/R/refmans/base/html/polyroot.html)
  * en fait il n'y a rien à installer il fait partie du base package
```R
> ar_coeffs
[1] 0.03424419 0.93240462 0.37124779 0.46445019 0.96430244 0.07966744
> ## Checking if the roots of the companion matrix for the ar_coeffs are outside the unit circle
> roots_ar = polyroot(ar_coeffs)
> roots_ar
[1]  -0.03725561+0.0000000i  -1.05117603-0.0000000i   0.30709194-0.9216623i   0.30709194+0.9216623i -11.62984896+0.0000000i
```
* vérifier l'ordre des coefficients arima et polyroot (todo)
## la génération finale sous [Generate](../../R/generateARMASeries.R)
# Vérification des racines
```R
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
```
* donne que au 18/07/2025 les racines AR sont dans le cercle
```bash
[1] "For the complex roof -0.037256+0.000000i the norm id 0.037256"
[1] "For the complex roof -1.051176+-0.000000i the norm id 1.051176"
[1] "For the complex roof 0.307092+-0.921662i the norm id 0.971477"
[1] "For the complex roof 0.307092+0.921662i the norm id 0.971477"
[1] "For the complex roof -11.629849+0.000000i the norm id 11.629849"
```
* les racines ma sont en deros du cercle
```bash
[1] "For the complex roof 0.485938+1.134162i the norm id 1.233880"
[1] "For the complex roof -0.903941+0.733699i the norm id 1.164227"
[1] "For the complex roof -0.903941+-0.733699i the norm id 1.164227"
[1] "For the complex roof 0.485938+-1.134162i the norm id 1.233880"
[1] "For the complex roof -5.572533+-0.000000i the norm id 5.572533"
```
* Il a aupravant refuse de créer ts.sim3 car
```bash
Erreur dans arima.sim(n = 200, list(ar = ar_coeffs, ma = ma_coeffs), rand.gen = function(n,  : 
  la partie 'ar' du mopdèle n'est pas stationaire
6.
stop("'ar' part of model is not stationary")
5.
ts.sim3 <- arima.sim(n=200, list(ar = ar_coeffs, ma = ma_coeffs), rand.gen = function(n, ...) sqrt(0.1796) * rt(n, df = 5)) at testARMASeries.R#9
4.
eval(ei, envir)
3.
eval(ei, envir)
2.
withVisible(eval(ei, envir))
1.
source("~/CONSULTANT/rcp217_project/R/testARMASeries.R")
```
* pas besoin de calculer les Racines de la matrice companion R
 [Gerer les erreurs en R](https://www.geeksforgeeks.org/r-language/handling-errors-in-r-programming/)
 * faire des message parlants [la fonction sprintf](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/sprintf)
 * changer un booleen défini globalement [gestion des variables globale](https://www.w3schools.com/r/r_variables_global.asp)
 * Tous ces tests sont sous [Le fichier R de test](../../R/testARMASeries.R)
## Boucler en divisan par 2 un oeffcient au hasard
* créer une [fonction R](https://www.w3schools.com/r/r_functions.asp) qui génère une TimeSerie stationaire
  * elle prend en paramètre le nombre de points
  * d'après le site [rpubs](https://rpubs.com/StatMind2023/ar_mac_01) on peut générér des arima.sim uniquement avec les ordres c=(x[1],0, x[2])