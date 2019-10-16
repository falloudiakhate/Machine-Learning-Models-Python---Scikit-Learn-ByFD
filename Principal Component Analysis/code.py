##########################################################################################
##########################################################################################
##################                                                          ##############
##################  PRINCIPAL COMPONENTS ANALYSIS (PCA) @ByFD October 2019  ##############
##################                                                          ##############
##########################################################################################
##########################################################################################

                  ##########################################################
                  ################ PCA WITH PYTHON ONLY ####################
                  ##########################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
==========================================================================================

Data = pd.read_csv("my_courses.csv") #Lectures des donnees brutes

===========================================================================================

Data_cleaned = Data.fillna ( Data . mean ()) #Nettoyage des donnees

============================================================================================

Data_cleaned.describe() #Statistiques des donnees

============================================================================================

Data_pca = Data_cleaned[["inscription","progression","moyenneDeClasse","duree","difficulte","nbChapitres","ratioQuizEvaluation","nbEvaluations"]]

============================================================================================

Data_pca_standard = (Data_pca - Data_pca.mean())/Data_pca.std() #Donnees Centrees-Reduites

=============================================================================================

Data_pca_standard = np.matrix(Data_pca_standard) #Lamatrice de donnees

=============================================================================================

U, Singular_value, Principal_components = np.linalg.svd(Data_pca_standard) #Utilisation oof SVD to calculate The principal components

=============================================================================================

Principal_components[0] #The first Principal Components

=============================================================================================

Eigenvalues = (Singular_value * Singular_value)/(np.shape(Data_pca_standard)[0] - 2) #Valeur propres de la matrice de donees

==============================================================================================

explained_variance_ratio  = Eigenvalues/sum(Eigenvalues) #Taux de variance expliquee

===============================================================================================

plt.plot(explained_variance_ratio, "b")

===============================================================================================

Principal_components_4 = Principal_components.T[:,:4] #Projections des donnees dur l'hyperplan factoriel (4 composantes prinsipales)

================================================================================================

Data_projected = Data_pca_standard * Principal_components_4

=================================================================================================

Data_projected_frame = pd.DataFrame(Data_projected, columns = ['A', 'B', 'C', 'D'])

==================================================================================================




                      ##########################################################
                      ################ PCA WITH SCIKIT-LEARN ###################
                      ##########################################################


import pandas as pd
import numpy as np
from sklearn import decomposition
from sklearn import preprocessing
from functions import *

==============================================================================================

std_scale = preprocessing.StandardScaler().fit(Data_pca)
Data_scaled = std_scale.transform(Data_pca)

=================================================================================================

pca = decomposition.PCA(n_components=6)
pca.fit(Data_scaled)

=================================================================================================

pca.components_
pca.explained_variance_
pca.explained_variance_ratio_

=================================================================================================

plt.plot(pca.explained_variance_ratio_, "b")

==================================================================================================

Data_projected_ = pca.transform(Data_scaled)

===================================================================================================

Data_projected_frame_= pd.DataFrame(Data_projected_, columns = ['A', 'B', 'C', 'D', "E", "F"])

===================================================================================================

pcs = pca.components_
display_circles(pcs, 6 , pca, [(0,1),(2,3),(4,5)], labels = np.array(Data_pca.columns))

===================================================================================================
