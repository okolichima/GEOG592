library(tmap)
library(rgdal)
me <- readOGR ("./", "Income")
 qtm(me, fill="Income", fill.style="quantile", 
+     fill.n=4,
+     fill.palette="Greens",
+     legend.text.size = 0.5,
+     layout.legend.position = c("right", "bottom"))

