library(KAML)
KAML.Data(vfile=c(paste0("/mnt/home/zhengjul/class/frontiers/data/widiv_SNP/chr",i,"_pruned.vcf")),out="maize",sep="\t",SNP.impute=c("Middle"), maxLine=1000, priority="speed")
for (j in 1:5){
mykaml <- KAML(pfile="../combined_traits_tar_pruned_id.csv", pheno=j,gfile="maize", Top.num=15, Top.perc=c(0.00001,0.1), cpu=1, sample.num = 1, crv.num = 3)
}

