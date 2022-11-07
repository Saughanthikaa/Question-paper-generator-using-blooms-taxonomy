import tabula

#data = tabula.read_pdf("dbms.pdf",pages="all")

#print(data)
tabula.convert_into("dbms.pdf","dbms.csv",pages="all",output_format="csv")