#R code to convert PDF to text.
#run Rscript pdf_text.r >> r_output.txt

library(pdftools)
text <- pdf_text("./CRViewReport_ 29271204402.pdf")
text2 <- strsplit(text, "\n")
# line <- text2[1]
print(text2[1])