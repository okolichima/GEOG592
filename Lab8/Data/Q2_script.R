library(tmap)
library(tmap)
library(rgdal)
library(dplyr)
library(raster)
library(rgeos)

me <- readOGR("./Data", "Income")

qtm(me, fill ="Income", fill.style ="quantile", 
    +     fill.n = 4,
    +     fill.palette ="Greens",
    +     legend.text.size = 0.5,
    +     layout.legend.position = c("right", "bottom"))

Aug_ll <- readOGR("./Data", "Augusta_ll")
proj4string(Aug_ll)
Aug_UTM <- spTransform(Aug_ll, CRS("+init=epsg:26919"))
Aug_UTM <- spTransform(Aug_ll, CRS("+proj=utm +zone=19 +datum=NAD83 +units=m +no_defs +ellps=GRS80 +towgs84=0,0,0"))

d50 <- buffer(Aug_UTM, width=50000, quadsegs=10)
d100 <- buffer(Aug_UTM, width=100000, quadsegs=10)
d150 <- buffer(Aug_UTM, width=150000, quadsegs=10)
d200 <- buffer(Aug_UTM, width=200000, quadsegs=10)
d300 <- buffer(Aug_UTM, width=300000, quadsegs=10)

tm_shape(d300) +tm_borders() +tm_shape(d200) +tm_borders() + tm_shape(d150) +tm_borders() + tm_shape(d100) +tm_borders() + tm_shape(d50) +tm_borders() +tm_shape(me) +tm_borders()
dAll <- union(d50, d100)
dAll <- union(d150, dAll)
dAll <- union(d200, dAll)
dAll <- union(d300, dAll)
dAll$ID <- 1:length(dAll)
dAllme <- crop(dAll, me)

library(rgeos)
dAllme$Area_band <- gArea(dAllme, byid=TRUE) / 1000000

qtm(dAllme, fill="Area_band")

clp1 <- intersect(me, dAllme)
tm_shape(clp1) + tm_fill(col="Income") + tm_borders()

clp1$Area_sub <- gArea(clp1, byid=TRUE) / 1000000

clp1$frac_area <- clp1$Area_sub / clp1$Area_band

clp1$wgt_inc <- clp1$Income * clp1$frac_area

dist_inc <- aggregate(clp1, by="ID",sums= list(list(sum, "wgt_inc")))
qtm(dist_inc, fill="wgt_inc") 
