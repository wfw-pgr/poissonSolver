import sys
import numpy                      as np
import nkUtilities.load__config   as lcf
import nkUtilities.cMapTri        as cmt
import nkUtilities.configSettings as cfs


# ========================================================= #
# ===  display                                          === #
# ========================================================= #
def display():
    
    # ------------------------------------------------- #
    # --- [1] Arguments                             --- #
    # ------------------------------------------------- #
    config   = lcf.load__config()
    datFile1 = "dat/result.dat"
    datFile2 = "dat/source.dat"
    pngFile1 = datFile1.replace( "dat", "png" )
    pngFile2 = datFile2.replace( "dat", "png" )

    # ------------------------------------------------- #
    # --- [2] Fetch Data                            --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    Data1  = lpf.load__pointFile( inpFile=datFile1, returnType="point" )
    xAxis1 = Data1[:,0]
    yAxis1 = Data1[:,1]
    zAxis1 = Data1[:,2]

    info   = lpf.load__pointFile( inpFile=datFile2, returnType="info"  )
    Data2  = lpf.load__pointFile( inpFile=datFile2, returnType="point" )
    xAxis2 = Data2[:,0]
    yAxis2 = Data2[:,1]
    zAxis2 = Data2[:,2]
    LJ, LI = info["shape"][1], info["shape"][2]

    Data_        = np.zeros( (LJ,LI,3) )
    Data_[:,:,0] = 0.0
    Data_[:,:,1] = 0.0
    Data_[:,:,2] = np.reshape( Data1[:,2], (LJ,LI) )
    x1Axis       = np.reshape( xAxis1    , (LJ,LI) )
    x2Axis       = np.reshape( yAxis1    , (LJ,LI) )
    
    import nkBasicAlgs.calc__curl2d as crl
    curl         = crl.calc__curl2d( Data=Data_, x1Axis=x1Axis, x2Axis=x2Axis, coordinate="xyz" )
    xvec         = np.copy( np.reshape( curl[:,:,0], (-1,) ) )
    yvec         = np.copy( np.reshape( curl[:,:,1], (-1,) ) )
    print( xvec.shape, yvec.shape, xAxis1.shape, yAxis1.shape, zAxis1.shape )
    
    # ------------------------------------------------- #
    # --- [3] config Settings                       --- #
    # ------------------------------------------------- #
    cfs.configSettings( configType="cMap_def", config=config )
    config["FigSize"]        = (5,5)
    config["cmp_position"]   = [0.16,0.12,0.97,0.88]
    config["xTitle"]         = "X (m)"
    config["yTitle"]         = "Y (m)"
    config["cmp_xAutoRange"] = True
    config["cmp_yAutoRange"] = True
    config["cmp_xRange"]     = [-5.0,+5.0]
    config["cmp_yRange"]     = [-5.0,+5.0]

    # ------------------------------------------------- #
    # --- [4] plot Figure                           --- #
    # ------------------------------------------------- #
    cmt.cMapTri( xAxis=xAxis1, yAxis=yAxis1, cMap=zAxis1, xvec=xvec, yvec=yvec, \
                 pngFile=pngFile1, config=config )
    cmt.cMapTri( xAxis=xAxis2, yAxis=yAxis2, cMap=zAxis2, pngFile=pngFile2, config=config )


# ======================================== #
# ===  実行部                          === #
# ======================================== #
if ( __name__=="__main__" ):
    display()

