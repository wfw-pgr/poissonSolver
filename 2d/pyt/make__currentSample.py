import numpy as np


# ========================================================= #
# ===  make__currentSample.py                           === #
# ========================================================= #

def make__currentSample():

    # ------------------------------------------------- #
    # --- [1] prepare grid                          --- #
    # ------------------------------------------------- #
    x_,y_,z_      = 0, 1, 2
    outFile       = "dat/source.dat"
    import nkUtilities.equiSpaceGrid as esg
    x1MinMaxNum   = [ -1.0, +1.0, 21 ]
    x2MinMaxNum   = [ -1.0, +1.0, 21 ]
    x3MinMaxNum   = [  0.0,  0.0,  1 ]
    ret           = esg.equiSpaceGrid( x1MinMaxNum=x1MinMaxNum, x2MinMaxNum=x2MinMaxNum, \
                                       x3MinMaxNum=x3MinMaxNum, returnType = "structured" )

    # ------------------------------------------------- #
    # --- [2] prepare distribution                  --- #
    # ------------------------------------------------- #
    jtype         = "uniform"
    radius        = 0.3
    j0            = 1.0
    current       = np.zeros( ( ret.shape[0], ret.shape[1], ret.shape[2] ) )
    radii         = np.sqrt( ret[:,:,:,x_]**2 + ret[:,:,:,y_]**2 )
    index         = np.where( radii <= radius )

    # ------------------------------------------------- #
    # --- [3] define current distribution           --- #
    # ------------------------------------------------- #
    if   ( jtype == "uniform" ):
        current[index]  = j0
        ret[:,:,:,z_]   = current
    elif ( jtype == "linear"  ):
        current[index]  = j0 * ( radius - radii ) / ( radius - 0.0 )
        ret[:,:,:,z_]   = current
    else:
        sys.exit( "[make__currentSample.py] jtype == ??? " )

    # ------------------------------------------------- #
    # --- [4] set boundary condition                --- #
    # ------------------------------------------------- #
    ret[:, 0, :,z_]     = 0.0
    ret[:,-1, :,z_]     = 0.0
    ret[:, :, 0,z_]     = 0.0
    ret[:, :,-1,z_]     = 0.0
    
    import nkUtilities.save__pointFile as spf
    spf.save__pointFile( outFile=outFile, Data=ret )
    
    return()


# ========================================================= #
# ===   実行部                                          === #
# ========================================================= #

if ( __name__=="__main__" ):
    make__currentSample()
