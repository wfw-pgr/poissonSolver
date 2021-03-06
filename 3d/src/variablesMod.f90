module variablesMod
  
  implicit none
  integer         , parameter   :: cLen     = 300
  integer         , parameter   :: lun      = 50
  double precision, parameter   :: eps      = 1.e-8
  integer                       :: LI, LJ, LK, nCmp
  double precision              :: dx, dy, dz
  double precision, allocatable :: xvec(:,:,:), source(:,:,:), xg(:,:,:), yg(:,:,:), zg(:,:,:)
  character(cLen) , parameter   :: srcFile  = "dat/source.dat"
  character(cLen) , parameter   :: rslFile  = "dat/result.dat"

  integer                       :: myRank, PEtot, ierr
  
end module variablesMod
