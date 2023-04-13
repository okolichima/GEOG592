setwd("C:/Users/Chima Okoli/GEOG592/Lab8/Data")
library(tmap)
library(rgdal)
library(dplyr)
library(raster)
library(ggplot2)
gas_prices <- read.csv("gas.csv")
states <- readOGR("STATES.shp")
states_gas <- left_join(me@data, dat, by=c("NAME" = "County"))
states_gas <- merge(states, gas_prices, by.x = "STATE_NAME", by.y = "State", all.x = TRUE)
breaks <- c(3.00, 3.50, 4.00, 4.50, 5.00, Inf)
pal <- c("#fee5d9", "#fcbba1", "#fc9272", "#fb6a4a", "#de2d26", "#a50f15")
tm_shape(states_gas) +
+     tm_polygons(col = "Regular", palette = pal, breaks = breaks, border.col = "grey50") +
+     tm_layout(legend.outside.position = "bottom", legend.outside = TRUE)

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