#########################################################################################################
#########################################################################################################
#######################                                                           #######################
#######################                   MODULE ACM CODE AVEC PYTHON             #######################
#######################                                                           #######################
#######################           AUTHOR : Fallou DIAKHATE @BYFD Octobre 2019     #######################
#######################                                                           #######################
#########################################################################################################
#########################################################################################################


# The acm class
class ACM(object):


        def __init__(self, X):

            self.X = X


        # Contingence Table function
        def Con_table(self):

                Dic = {}

                for i in self.X.columns:
                    Dic.update({i : self.X[i].sum()})

                r_marge = pd.DataFrame(Dic, index = ["row_marge"])
                df1 = pd.concat([self.X, r_marge])

                L = []

                for i in df1.T.columns:
                    L.append(df1.T[i].sum())

                l_marge = pd.DataFrame(L, index = df1.index, columns = ["line_marge"])
                con_table = pd.concat([df1, l_marge], axis=1)

                return con_table


        # Frequency Table function
        def Freq_table(self):

                con_table = self.Con_table()
                Data = np.c_[con_table]

                for i in np.linspace(0, con_table.shape[0] - 1,con_table.shape[0], dtype = "int"):
                    for j in np.linspace(0, con_table.shape[1]-1,con_table.shape[1], dtype = "int" ):
                        Data[i, j] = Data[i, j] / Data[con_table.shape[0] - 1, con_table.shape[1] - 1]

                freq_table = pd.DataFrame(Data, columns = con_table.columns, index = con_table.index)

                return freq_table

        # Row Profil  function
        def Profil_ligne(self):

                con_table = self.Con_table()
                Data = np.c_[con_table]

                for i in np.linspace(0, con_table.shape[0] - 1,con_table.shape[0], dtype = "int"):
                    for j in np.linspace(0, con_table.shape[1]-1,con_table.shape[1], dtype = "int" ):
                        Data[i, j] = Data[i, j] / Data[i, con_table.shape[1] - 1]

                profile_ligne = pd.DataFrame(Data, columns = con_table.columns, index = con_table.index)
                profile_ligne = profile_ligne.drop("row_marge")
                profile_ligne = profile_ligne.drop("line_marge", axis = 1)

                return  profile_ligne


        # Column Profil function
        def Profil_colone(self):

                con_table = self.Con_table()
                Data = np.c_[con_table]

                for i in np.linspace(0, con_table.shape[0] - 1,con_table.shape[0], dtype = "int"):
                    for j in np.linspace(0, con_table.shape[1]-1,con_table.shape[1], dtype = "int" ):
                        Data[i, j] = Data[i, j] / Data[con_table.shape[0] - 1, j]

                profile_colone = pd.DataFrame(Data, columns = con_table.columns, index = con_table.index)
                profile_colone = profile_colone.drop("row_marge")
                profile_colone = profile_colone.drop("line_marge", axis = 1)

                return  profile_colone


