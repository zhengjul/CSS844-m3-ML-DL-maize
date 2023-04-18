library(KAML)

for (i in 1:10){
 print(i)
 KAML.Data(vfile=c(paste0("~/class/frontiers/data/widiv_SNP/chr",i,"_pruned.vcf")),out=paste0("maize",i),sep="\t",SNP.impute=c("Middle"), maxLine=1000, priority="memory")
 for (j in 1:5){
  mykaml <- KAML(pfile="combined_traits_tar_pruned_id.csv", pheno=j,gfile=paste0("maize",i), Top.num=NULL, Top.perc=NULL)
 }
}

