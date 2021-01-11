import numpy as np


# ========================================================= #
# ===  make__currentSample.py                           === #
# ========================================================= #

def make__currentSample():

    # ------------------------------------------------- #
    # --- [1] prepare grid                          --- #
    # ------------------------------------------------- #
    x_,y_,z_,v_   = 0, 1, 2, 3
    outFile       = "dat/source.dat"
    import nkUtilities.equiSpaceGrid as esg
    x1MinMaxNum   = [ -1.0, +1.0, 21 ]
    x2MinMaxNum   = [ -1.0, +1.0, 21 ]
    x3MinMaxNum   = [ -1.0, +1.0, 21 ]
    ret           = esg.equiSpaceGrid( x1MinMaxNum=x1MinMaxNum, x2MinMaxNum=x2MinMaxNum, \
                                       x3MinMaxNum=x3MinMaxNum, returnType = "structured" )
    
    # ------------------------------------------------- #
    # --- [2] prepare distribution                  --- #
    # ------------------------------------------------- #
    ctype         = "uniform"
    radius        = 0.3
    rho0          = 1.0
    charge        = np.zeros( ( ret.shape[0], ret.shape[1], ret.shape[2] ) )
    radii         = np.sqrt( ret[:,:,:,x_]**2 + ret[:,:,:,y_]**2 + ret[:,:,:,z_]**2 )
    index         = np.where( radii <= radius )
    Data          = np.zeros( (ret.shape[0],ret.shape[1],ret.shape[2],4) )
    Data[...,0:3] = ret[...]

    # ------------------------------------------------- #
    # --- [3] define current distribution           --- #
    # ------------------------------------------------- #
    if   ( ctype == "uniform" ):
        charge[index]  = rho0
        Data[...,v_]   = charge
    elif ( jtype == "linear"  ):
        charge[index]  = rho0 * ( radius - radii ) / ( radius - 0.0 )
        Data[...,v_]   = charge
    else:
        sys.exit( "[make__currentSample.py] jtype == ??? " )

    # ------------------------------------------------- #
    # --- [4] set boundary condition                --- #
    # ------------------------------------------------- #
    Data[ 0, :, :,v_]     = 0.0
    Data[-1, :, :,v_]     = 0.0
    Data[ :, 0, :,v_]     = 0.0
    Data[ :,-1, :,v_]     = 0.0
    Data[ :, :, 0,v_]     = 0.0
    Data[ :, :,-1,v_]     = 0.0
    
    import nkUtilities.save__pointFile as spf
    spf.save__pointFile( outFile=outFile, Data=Data )
    
    return()


# ========================================================= #
# ===   実行部                                          === #
# ========================================================= #

if ( __name__=="__main__" ):
    make__currentSample()
