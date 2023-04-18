library(randomForest)
setwd("C:/Users/zhuor/Downloads/module3-corn2021")
df <- read.csv("kernel_phenolics_mean.csv")
df[is.na(df)] <- 0
df <-df[ , !(names(df) %in% "Accession")]
fit = randomForest(as.factor(LineName) ~ .,data=df,importance=TRUE)
varImpPlot(fit) 
importance(fit,scale=TRUE) 

df <- read.csv("tar_spot_supplemental.csv")
df[is.na(df)] <- 0
df <-df[ , !(names(df) %in% c("Accession", "Year", "Subpopulation", "Field"))]
fit = randomForest(as.factor(Genotype) ~ .,data=df,importance=TRUE)
varImpPlot(fit) 
importance(fit,scale=TRUE) 
