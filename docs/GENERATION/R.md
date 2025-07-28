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
* Non on ne peut pas
```R
x <- sample.int(10, 2, replace=TRUE) # p <- x[1], q <- x[2]
p <- x[1]
q <- x[2]
ts.sim10 <- arima.sim(n=200, model = list(order = c(p,0,q)), rand.gen = function(n, ...) sqrt(0.1796) * rt(n, df = 5))
ts.plot(ts.sim10)
```
* me répond que 
```bash
Error in arima.sim(n = 200, model = list(order = c(p, 0, q)), rand.gen = function(n,  : 
  inconsistent specification of 'ar' order
```
* Il faut donner les ar et ma coefficients !!!
## Créer une fonction qu génère des coefficients en dehors du cercle
* C'est le but de [test de Génération Méthode 1](../../R/testGenerateARMASeries_methode1.R) mais même si mes racines sont en dehors du cercle
  * arima.sim me répond
```bash
Error in arima.sim(model = list(order = c(4, 0, 0), ar = ar_coeffs), n = 200) : 
  'ar' part of model is not stationary
2.
stop("'ar' part of model is not stationary")
1.
arima.sim(model = list(order = c(4, 0, 0), ar = ar_coeffs), n = 200)
```
## Relancer le arima.sim autant de fois que nécessaire
cf. [test général des ARMA Series](../../R/testARMASeries.R)
* C'est l'objet de [test de Génération Méthode 2](../../R/testGenerateARMASeries_methode2.R)
 * retourner un dict contenant le ar et ma coefficient ainsi que la time serie (todo)
 * Les listes R sont mes amies
```R
y <- LETTERS[1:10]
> y
 [1] "A" "B" "C" "D" "E" "F" "G" "H" "I" "J"
> x <- 1:3
> x
[1] 1 2 3
> my_list <- list(coeff=x,data=y) # cf. Python dictionaries
> my_list[['coeff']] # Pour le premier niveau utiliser les doubles brackets
[1] 1 2 3 # c'est un vector
> my_list[['coeff']][2]
[1] 2 # c'est un vecteur unitaire ou un entier
> my_list[['coeff']][[2]]
[1] 2 # même résultat que précédemment
```
# Conclusion ce samedi 19/07/2025 à 17h
* Le code fonctionne
```R
my_ts <- calculate_times_serie(4,5)
arma1 = my_ts[[3]]
ts.plot(arma1)
```
## NB 
* dans arima.sim le order=c(p,0,q) ne fonctionne pas, on donne directement les ar et les ma coefficients
* Pour accéder aux différentes parties de la liste dans la console et le code R passer par les indices (qui commencent à 1) et non par les entrées du dictionnaire
```R
> my_ts[['ar_coefficients']]
NULL
> my_ts[[1]]
[1] 0.1092415 0.3497106 0.2525748 0.1406372
> my_ts[[2]]
[1] 0.7967161 0.6926423 0.1887584 0.9610122 0.6902769
> my_ts[[3]]
Time Series:
Start = 1 
End = 200 
Frequency = 1 
  [1]   7.45438713   6.16172410   6.17463007   6.05140955   5.57350931   1.85552825   1.83457581   2.67188012   1.83783567   1.18452208
 [11]   0.17797997   0.97789176   0.99913365   1.41919738  -0.41166497  -0.77101924   2.44175196  -0.71287187   0.54371471   0.01098280
 [21]   0.79571980  -0.81205788  -1.51658554  -1.36912269  -3.85088685  -2.56064349  -3.23340994  -3.50781488  -5.41202106  -5.65746315
 ## Et ainsi jusqu'à 200 valeurs
```
* voir comment on obtient les points de la time serie
```R
> arma1[[1]]
[1] 7.454387 # on obtient vraiment le premier élément, on a juste un problème de précision
> arma1[1] # double ou simple donne le même résultat
[1] 7.454387
> length(arma1) # se comporte comme un vecteur
[1] 200
```
## car mettre ces données dans un fichier CSV qui sera nommé avec p et q et un indice (todo)
* Il faut d'abord tranposer le tableau généré cf. réponse 25 de ce [Post de post de StackOverflow](https://stackoverflow.com/questions/33643181/how-do-i-flip-rows-and-columns-in-r)
* ce qui donne
```R
my_ts <- calculate_times_serie(4,5)
arma1 = my_ts[[3]]
ts.plot(arma1)
# write.table(t(arma1), file="C:/Images/test.csv", sep=";") # on windows
write.table(t(arma1), file = "~/test.csv", fileEncoding = "UTF-8", sep=";") #t(arma1) for transposing the DataFrame arma1 
```
# Générer des fichiers dans un répertoire
## nom du répertoire
* [gérer les dates en R](https://demandred.gitbooks.io/introduction-a-r-pour-les-chatons/content/les-structures-de-donnees-avancees/les-dates-en-r.html)
  * ou plutôt [formatter dates](https://campus.datacamp.com/courses/intermediate-r/chapter-5-utilities?ex=14)
```R
> ftoday <- format(Sys.Date(), format = "%d%m%Y")
# idem avec TimeStamp
> now <- Sys.time()
> fNow <- format(now, format="%d%m%Y_%H%M%S")
> fNow
[1] "28072025_181246"
```