library(rgdal)
me <- readOGR("./Data", "Income")

qtm(me, fill="Income", fill.style="quantile", 
    fill.n=4,
    fill.palette="Greens",
    legend.text.size = 0.5,
    layout.legend.position = c("right", "bottom"))

tm_shape(me) + 
  tm_fill("Income", style="fixed", breaks=c(0,23000 ,27000,100000 ),
          labels=c("under $23,000", "$23,000 to $27,000", "above $27,000"),
          palette="Greens")  +
  tm_borders("grey") +
  tm_legend(outside = TRUE, text.size = .8) +
  tm_layout(frame = TRUE)

dat <- read.csv("./Data/Crime2012.csv")
library(dplyr)
me@data <- left_join(me@data, dat, by=c("NAME" = "County"))
me$Violent_rate <- me$Violent / me$Population * 100000
qtm(me, fill="Violent_rate", fill.style="pretty", title="Violent crimes \nper 100,000", legend.outside=TRUE)

library(raster)
dem <- raster("./Data/DEM.img")
tm_shape(dem) + tm_raster(palette = "Greys", n=8) +
  tm_legend(outside = TRUE, text.size = .8)

slope  <- terrain(dem, opt='slope')
aspect <- terrain(dem, opt='aspect')
hill   <- hillShade(slope, aspect, 40, 270)
tm_shape(hill) + tm_raster(palette = "Greys", style="cont", contrast = c(0,.8)) +
  tm_legend(show=FALSE)

hill_me <- mask(hill, me)
tm_shape(hill_me) + tm_raster(palette = "Greys", style="cont", contrast = c(0,.8)) +
  tm_legend(show=FALSE) 

tm_shape(me) + 
  tm_fill("Income", style="fixed", breaks=c(0,23000 ,27000,100000 ),
          labels=c("under $23,000", "$23,000 to $27,000", "above $27,000"),
          palette="Greens")  +
  tm_borders("grey") +
  tm_legend(outside = TRUE, text.size = .8) +
  tm_layout(frame = FALSE) +
  tm_shape(hill_me) + tm_raster(palette = "Greys", style="cont", 
                                contrast = c(0,.8), alpha=0.4, 
                                legend.show = FALSE) 

tm_shape(me) + 
  tm_fill("Income", style="fixed", breaks=c(0,23000 ,27000,100000 ),
          labels=c("under $23,000", "$23,000 to $27,000", "above $27,000"),
          palette="Greens")  +
  tm_borders("grey") +
  tm_legend(outside = TRUE, text.size = .8) +
  tm_layout(frame = FALSE) +
  tm_shape(hill_me) + tm_raster(palette = "Greys", style="cont", 
                                contrast = c(0,.8), alpha=0.4, 
                                legend.show = FALSE) 

tm_shape(me) + 
  tm_fill("Income", style="fixed", breaks=c(0,23000 ,27000,100000 ),
          labels=c("under $23,000", "$23,000 to $27,000", "above $27,000"),
          palette="Greens")  +
  tm_borders("grey") +
  tm_legend(outside = TRUE, text.size = .8) +
  tm_layout(frame = FALSE) +
  tm_shape(hill_me) + tm_raster(palette = "Greys", style="cont", 
                                contrast = c(0,.8), alpha=0.4, 
                                legend.show = FALSE)

me$Cutoff <- ifelse( me$Income > 23000, 1, 0)
qtm(me, fill="Cutoff", fill.style="cat")

me_dis <- aggregate(me, by="Cutoff")
qtm(me_dis, fill="Cutoff", fill.style="cat")

tm_shape(d300) +tm_borders() +tm_shape(d200) +tm_borders() + tm_shape(d150) +tm_borders() + tm_shape(d100) +tm_borders() + tm_shape(d50) +tm_borders() +tm_shape(me) +tm_borders()
dAll <- union(d50, d100)
dAll <- union(d150, d200)
dAll <- union(d300, dAll)
dAll$ID <- 1:length(dAll)
dAllme <- crop(dAll, me)

library(rgeos)
dAllme$Area_band <- gArea(dAllme, byid=TRUE) / 1000000

qtm(dAllme, fill="Area_band")

clp1 <- intersect(me, dAllme)
tm_shape(clp1) + tm_fill(col="Income") + tm_borders()