library(tmap)
library(rgdal)
library(dplyr)
me <- readOGR("Counties.shp")
names(me)


tmap_options(check.and.fix = TRUE)
me$popchg <- (me$X1990 - me$X1980)/ me$X1980 * 100

qtm(me, fill="popchg", fill.style="quantile",
    fill.n=4,
    fill.palette="Blues",
    legend.text.size = 0.5,
    layout.legend.position = c("left", "bottom"))
