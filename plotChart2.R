library(ggplot2)
library(ggsci)
library(dplyr)
library(reshape2)
library(tidygraph)
library(tidyverse)
library(wesanderson)
library(ggpubr)
library(grid)
setwd("/media/ganesh/RA/KSU/NGS/smallRNAseq/JeffUrilydation/TIE_/filtereMiRs/")
#args = commandArgs(trailingOnly=TRUE)
mirinput = read.table("FinalmiRs.txt", sep = "\t", header = TRUE, strip.white = TRUE, na.strings = TRUE)
#mirinput = read.table("let-7b-3p.miRNA.Cancer_meantissue.Grouped.txt", sep = "\t", header = TRUE, strip.white = TRUE, na.strings = TRUE)
#mirinput = read.table("miRNA-23b-3p-TTGCCAGGGATTA-align.txt_uridylated.txt.Cancer_meantissueFinal.txt", sep = "\t", header = TRUE, strip.white = TRUE, na.strings = TRUE)
#mirinput = read.table("miRNA-324-3p-GCCCCAGGTGCTG-align.txt_uridylated.txt.Cancer_meantissueFinal.txt", sep = "\t", header = TRUE, strip.white = TRUE, na.strings = TRUE)
#mirinput = read.table("miRNA-148b-3p-TGCATCACAGAAC-align.txt_uridylated.txt.Cancer_meantissueFinal.txt", sep = "\t", header = TRUE, strip.white = TRUE, na.strings = TRUE)
head(mirinput)
#colnames(mirinput) = sub("\\.", "", colnames(mirinput))
#colnames(mirinput) = sub("\\ ", ".", colnames(mirinput))
mir2 = reshape2::melt(mirinput)
head(mir2)
colnames(mir2) = c("featuretype","miR","Cancertype","Tissue","Expression")
#mir2$sd = sqrt(var(mir2$Expression))
mir2$Expression = log10(mir2$Expression)
#mir2$sd = log10(mir2$sd)

#View(mir2)

#mir2$Tissue = sub("\\.", " ", mir2$Tissue)
#mir2$Tissue = sub("\\_", "-", mir2$Tissue)

#png(file=args[2],width=1600, height=1200, units="px", pointsize=24, res=100)

colourCount = length(unique(mir2$Tissue))
getPalette = colorRampPalette(brewer.pal(9, "Set1"))

grobmir <- grobTree(textGrob("miRNA Expression", x=0.5,  y=0.05, hjust=0,
                          gp=gpar(col="red", fontsize=13, fontface="bold")))

grobiso <- grobTree(textGrob("isomiR Expression", x=0.5,  y=0.95, hjust=0,
                             gp=gpar(col="red", fontsize=13, fontface="bold")))

ggplot(mir2, aes(x=Cancertype, y=Expression, fill=Tissue)) +
         geom_bar(stat="identity", alpha=0.7) + theme_minimal() + 
         theme(axis.text.x = element_text(size=6, angle = 45, hjust=1, face = "bold")) +
          theme(axis.text.y = element_text(size=6, angle = 0, hjust=0, face = "bold")) +
  scale_fill_manual(values = colorRampPalette(brewer.pal(length(unique(mir2$Tissue)), "Paired"))(colourCount)) +
  theme(axis.line = element_line(size=.5, colour = "black"), axis.ticks = element_line(size=0.5)) + 
  theme(legend.position = "bottom", legend.justification = c(0,.75), legend.box.margin = margin(c(-5,0,-5,-15)), legend.background=element_blank()) + 
  theme(legend.title = element_text(face="bold", size=10, vjust=1), legend.text = element_text(face="bold", size=5, angle=0), legend.key.size=unit(.5, "line")) + 
  labs(fill="") + xlab("Cancer types") + ylab("log10 (Expression)") + geom_hline(yintercept = 0,) +
  theme(plot.title = element_text(hjust=0.5, face = "bold", size=10)) + ggtitle("Uridylated isomiRs/miR") + 
  theme(axis.title.x = element_text(hjust=0.5, vjust=-0.5, face = "bold", size=6), axis.title.y = element_text(hjust=0.5, vjust=-0.5, face = "bold", size=6)) +
  facet_wrap(~miR + featuretype, nrow=2) + 
  theme( strip.text = element_text(face = "bold", size = rel(.5)),
    strip.background = element_rect(fill = "lavender", colour = "black", size = 1))

ggsave("WholePlot.tiff", width = 2800, height = 2400, units = "px", bg = "white")

#geom_errorbar( aes(x=Cancertype, ymin=Expression-sd, ymax=Expression+sd), width=0.4, colour="black", alpha=0.5, size=.5) 
#annotation_custom(grobmir) + annotation_custom(grobiso) +   theme(panel.grid.major = element_blank()) +



#dev.off()
