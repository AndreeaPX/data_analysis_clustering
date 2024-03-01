import numpy as np
import pandas as pd
from hclust import hclust
from functii import  *
import seaborn as sns
from sklearn.decomposition import PCA
from geopandas import GeoDataFrame

#AM COMENTAT TOATE HISTOGRAMELE SI O PARTE DIN HARTI, DEOARECE ERAU PREA MULTE GRAFICE SI NU STIU DACA O SA MEARGA PE ORICE COMPUTER

data=pd.read_csv("unitati_invatamant.csv", index_col=0)
labels=list(data)
hclust_model = hclust(data, labels)

#Partitia optimala CU Bucuresti
optimal_partition_b = hclust_model.get_partition()
#Dendrograma
plt_hierarchy(hclust_model.h, data.index, hclust_model.threshold, "Plot ierarhie pentru partitia optimala incluzand Municipiul Bucuresti")
pca = PCA(2)
pca.fit(hclust_model.x)
z = pca.transform(hclust_model.x)
#plot instanțe pe clusteri în primele două axe principale (componente);
plt_partition(z,optimal_partition_b,"Plot partitie optimala incluzand Municipiul Bucuresti", data.index)
current_palette = sns.color_palette("spring_r",2)
#for v in labels:
#    plt_distributions(data[v].values, optimal_partition_b,v,current_palette )

#Histograma
#for i in range(len(labels)):
#    histogram(hclust_model.x[:, i], optimal_partition_b, labels[i])

#Harta
table_partitions = pd.DataFrame(data={
    "POpt": optimal_partition_b
}, index=data.index)
gdf = GeoDataFrame.from_file("RO_NUTS2/Ro.shp")
plt_map(gdf, table_partitions, "POpt", title="Partitia optimala cu ,unicipiul Bucuresti")

#Partitie de 4 CU BUCURESTI
p4_B = hclust_model.get_partition(4)
current_palette = sns.color_palette("spring_r",4)
#Dendrograma
plt_hierarchy(hclust_model.h, data.index, hclust_model.threshold, "Plot ierarhie pentru partitia de 4 incluzand Municipiul Bucuresti")
plt_partition(z,p4_B,"Plot partitie de 4 incluzand Municipiul Bucuresti", data.index)
#for v in labels:
#    plt_distributions(data[v].values, p4_B,v,current_palette )
#Histograma
#for i in range(len(labels)):
# histogram(hclust_model.x[:, i], p4_B, labels[i])

table_partitions["P4B"]=p4_B
#Harta
plt_map(gdf,table_partitions , "P4B", title="Partitia de 4")



#FARA BUCURESTI
data_table = pd.read_csv("unitati_invatamant.csv", index_col=0, skiprows=[4])
hclust_model = hclust(data_table, labels)
#data_table=noul set de date, FARA BUCURESTI
#Partitia optimala FARA Bucuresti
optimal_partition = hclust_model.get_partition()
plt_hierarchy(hclust_model.h, data_table.index, hclust_model.threshold, "Plot ierarhie pentru partitia optimala")
pca = PCA(2)
pca.fit(hclust_model.x)
z = pca.transform(hclust_model.x)
plt_partition(z,optimal_partition,"Plot partitie optimala", data_table.index)
current_palette = sns.color_palette("spring_r",2)
#for v in labels:
#    plt_distributions(data_table[v].values, optimal_partition,v,current_palette )

#Histograma
#for i in range(len(labels)):
#    histogram(hclust_model.x[:, i], optimal_partition, labels[i])

#Harta
table_of_partitions = pd.DataFrame(data={
    "Popt": optimal_partition
}, index=data_table.index)
plt_map(gdf, table_of_partitions, "Popt", title="Partitia optimala")

#Partitie de 3
p3 = hclust_model.get_partition(3)
current_palette = sns.color_palette("spring_r",3)
plt_hierarchy(hclust_model.h, data_table.index, hclust_model.threshold, "Plot ierarhie pentru partitia de 3")
plt_partition(z,p3,"Plot partitie de 3", data_table.index)
#for v in labels:
#    plt_distributions(data_table[v].values, p3,v,current_palette )
#Histograma
#for i in range(len(labels)):
#    histogram(hclust_model.x[:, i], p3, labels[i])

table_of_partitions["P3"]=p3
#Harta
plt_map(gdf,table_of_partitions , "P3", title="Partitia de 3")

#Partitie de 4
p4 = hclust_model.get_partition(4)
current_palette = sns.color_palette("spring_r",4)
plt_hierarchy(hclust_model.h, data_table.index, hclust_model.threshold, "Plot ierarhie pentru partitia de 4")
plt_partition(z,p4,"Plot partitie de 4", data_table.index)
#for v in labels:
#    plt_distributions(data_table[v].values, p4,v,current_palette )
#Histograma
#for i in range(len(labels)):
#    histogram(hclust_model.x[:, i], p4, labels[i])

table_of_partitions["P4"]=p4
#Harta
plt_map(gdf,table_of_partitions , "P4", title="Partitia de 4")


#PERSOANE INSCRISE IN ANUL 2020 PE NIVELE DE STUDIU
persoane=pd.read_csv("persoane_inscrise.csv", index_col=0)
etichete=list(persoane)
hclust_model_persoane = hclust(persoane, etichete)

#Partitia optimala
optPar = hclust_model_persoane.get_partition()
plt_hierarchy(hclust_model_persoane.h, persoane.index, hclust_model_persoane.threshold, "Plot ierarhie pentru partitia optimala a persoanelor inscrise la scoala")
pca_p = PCA(2)
pca_p.fit(hclust_model_persoane.x)
z_p = pca_p.transform(hclust_model_persoane.x)
plt_partition(z_p,optPar,"Plot partitie optimala a persoanelor inscrise la scoala", persoane.index)
current_palette = sns.color_palette("spring_r",3)
#for v in etichete:
#    plt_distributions(persoane[v].values, optPar,v,current_palette )

#Histograma
#for i in range(len(etichete)):
#    histogram(hclust_model_persoane.x[:, i], optPar, etichete[i])

#Harta
tabela_partitii = pd.DataFrame(data={
    "POpt": optPar
}, index=persoane.index)
#plt_map(gdf, tabela_partitii, "POpt", title="Partitia optimala")


#Partitie de 4
p4_persoane = hclust_model_persoane.get_partition(4)
current_palette = sns.color_palette("spring_r",4)
plt_hierarchy(hclust_model_persoane.h, persoane.index, hclust_model_persoane.threshold, "Plot ierarhie pentru partitia de 4 a persoanelor inscrise la scoala")
plt_partition(z_p,p4_persoane,"Plot partitie de 4 persoane inscrise la scoala", persoane.index)
#for v in etichete:
#    plt_distributions(persoane[v].values, p4_persoane,v,current_palette )
#Histograma
#for i in range(len(etichete)):
#    histogram(hclust_model_persoane.x[:, i], p4_persoane, etichete[i])

tabela_partitii["P4B"]=p4_persoane
#Harta
#plt_map(gdf,tabela_partitii , "P4B", title="Partitia de 4")


show()

#Salvare tabele in format .csv
table_partitions.to_csv("partitii_cu_Bucuresti.csv")
table_of_partitions.to_csv("partitii.csv")
tabela_partitii.to_csv("partitii_persoane.csv")