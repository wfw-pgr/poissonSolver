import numpy as np


# ========================================================= #
# ===  convert__vtsFile                                 === #
# ========================================================= #

def convert__vtsFile():

    inpFile1 = "dat/result.dat"
    inpFile2 = "dat/source.dat"
    import nkUtilities.load__pointFile as lpf
    Data1    = lpf.load__pointFile( inpFile=inpFile1, returnType="structured" )
    Data2    = lpf.load__pointFile( inpFile=inpFile2, returnType="structured" )
    
    Data     = np.concatenate( [Data1[:,:,:,0:4],Data2[:,:,:,3][:,:,:,None]], axis=3 )
    print( Data.shape )
    
    import nkVTKRoutines.convert__vtkStructuredGrid as vts
    outFile  = "png/out.vts"
    vts.convert__vtkStructuredGrid( Data=Data, outFile=outFile, names=["result","source"] )
    

# ========================================================= #
# ===   実行部                                          === #
# ========================================================= #

if ( __name__=="__main__" ):
    convert__vtsFile()
