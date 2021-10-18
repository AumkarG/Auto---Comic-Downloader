from PyPDF2 import PdfFileMerger
import os
name=input("Enter comic name : ")
pdfs=[i for i in os.listdir("Downloads/"+name) if i.endswith(".pdf")]
pdf_corrected=[]
for i in pdfs:
    if len(i)==5:
        pdf_corrected.append('0'+i)
    else:
        pdf_corrected.append(i)
pdf_corrected.sort()
pdfs=[i for i in pdf_corrected]
for i in range(6):
    pdf_subset=pdfs[i*4:i*4+4]
    merger = PdfFileMerger()

    for pdf in pdf_subset:
        print(pdf)
        if pdf.startswith('0'):
            pdf=pdf[1:]
        merger.append('Downloads/'+name+'/'+pdf)

    merger.write('Downloads/'+name+'/'+"result"+str(i)+".pdf")
    merger.close()
    print( "done")