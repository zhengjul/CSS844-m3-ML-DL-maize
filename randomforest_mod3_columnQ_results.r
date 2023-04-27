library(randomForest)
homedir="module3-corn2021"

df_all=data.frame()
clist = c("chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10")
for (j in clist){
  directory=paste0(homedir,"/columnQ_Debasemita_KAML_MLM_MR_brent/",j)
  direct<-list.files(directory, full.names = TRUE)
  i=paste0(directory,"/KAML.MaizeObsTarSpot.pred.txt")
  print(i)
  temp <- as.data.frame(read.csv(i))
  colnames(temp) <- j
  print(str(temp))
  if (nrow(df_all) == 0){
    df_all <- temp
  }
  else{
    df_all[,j]  <- temp 
  }
  
}
genotypes=paste0(homedir,"/columnQ_Debasemita_KAML_MLM_MR_brent/","combined_traits_tar_pruned.csv")
df <- as.data.frame(read.table(file = genotypes, sep = '\t', header = TRUE))
df_all$genotype <- df$common_name
fit = randomForest(as.factor(genotype) ~ .,data=df_all,importance=TRUE)
varImpPlot(fit) 
importance(fit,scale=TRUE) 

### RF on tar spot rating difference between observed and predicted phenotypes

df_all=data.frame()
clist = c("chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10")
for (j in clist){
  directory=paste0(homedir,"/columnQ_Debasemita_KAML_MLM_MR_brent/",j)
  direct<-list.files(directory, full.names = TRUE)
  i=paste0(directory,"/KAML.MaizeObsTarSpot.pred.txt")
  print(i)
  temp <- as.data.frame(read.csv(i))
  df1 <- as.data.frame(temp$MaizeObsTarSpot - df$MaizeObsTarSpot)
  colnames(df1) <- j
  
  print(str(df1))
  if (nrow(df_all) == 0){
    df_all <- df1
  }
  else{
    df_all[,j]  <- df1 
  }
  
}

df_all$genotype <- df$common_name
fit = randomForest(as.factor(genotype) ~ .,data=df_all,importance=TRUE)
varImpPlot(fit) 
importance(fit,scale=TRUE) 

### correlation analysis between weighted SNPs and the predicted phenotypes ###
corr_df=data.frame()
clist = c("chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10")
for (j in clist){
  directory=paste0(homedir,"/columnQ_Debasemita_KAML_MLM_MR_brent/",j)
  direct<-list.files(directory, full.names = TRUE)
  i=paste0(directory,"/KAML.MaizeObsTarSpot.pred.txt")
  df1 <- as.numeric(unlist(read.csv(i)))
  
  # i=paste0(directory,"/cv.p.csv")
  # temp <- as.data.frame(read.csv(i))
  # last_col <- temp$V1
  # df2 <- as.numeric(unlist(last_col))

  # Perform the correlation test
  corr <- cor.test(df1, df$MaizeObsTarSpot)
  
  # Extract the relevant values
  estimate <- corr$estimate
  p_value <- corr$p.value
  
  # Display the results
  cat("Estimated correlation coefficient:", round(estimate, 2), "\n")
  cat("P-value:", p_value, "\n")
  
}

#1.b. calculate correlation between observed and predicted phenotypes 
#one chromosome at a time, and see which chromosome gives the highest 
#accuracy - so "Which chromosome is most predictive of [your trait(s)]?" 
