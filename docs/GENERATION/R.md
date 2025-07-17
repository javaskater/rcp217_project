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