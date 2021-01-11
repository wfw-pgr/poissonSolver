module ioUtilityMod
contains
  
  ! ====================================================== !
  ! === load__source_and_boundary                      === !
  ! ====================================================== !
  subroutine load__source_and_boundary
    use variablesMod
    implicit none
    integer         :: i, j, k
    character(cLen) :: cmt

    ! ------------------------------------------------------ !
    ! --- [1] load Amatrix                               --- !
    ! ------------------------------------------------------ !
    open(lun,file=trim(srcFile),status="old")
    read(lun,*)
    read(lun,*)
    read(lun,*) cmt, LK, LJ, LI, nCmp
    allocate( source(LI,LJ,LK), xvec(LI,LJ,LK), xg(LI,LJ,LK), yg(LI,LJ,LK), zg(LI,LJ,LK) )
    xvec(:,:,:) = 0.d0
    do k=1, LK
       do j=1, LJ
          do i=1, LI
             read(lun,*) xg(i,j,k), yg(i,j,k), zg(i,j,k), source(i,j,k)
          enddo
       enddo
    enddo
    close(lun)
    write(6,*) "[load__source_and_boundary] srcFile is loaded...."

    ! ------------------------------------------------------ !
    ! --- [2] define delta :: dx, dy, dz                 --- !
    ! ------------------------------------------------------ !
    dx = xg(2,1,1) - xg(1,1,1)
    dy = yg(1,2,1) - yg(1,1,1)
    dz = zg(1,1,2) - zg(1,1,1)
    
    return
  end subroutine load__source_and_boundary
  

  ! ====================================================== !
  ! === save results in a file                         === !
  ! ====================================================== !
  subroutine save__results
    use variablesMod
    implicit none
    integer            :: i, j, k

    ! ------------------------------------------------------ !
    ! --- [1] save results                               --- !
    ! ------------------------------------------------------ !
    open(lun,file=trim(rslFile),status="replace")
    write(lun,"(a)") "# xg yg zg phi"
    write(lun,"(a,1x,2(i10))") "#", LK*LJ*LI, nCmp
    write(lun,"(a,1x,4(i10))") "#", LK, LJ, LI, nCmp
    do k=1, LK
       do j=1, LJ
          do i=1, LI
             write(lun,"(4(e15.8,1x))") xg(i,j,k), yg(i,j,k), zg(i,j,k), xvec(i,j,k)
          enddo
       enddo
    enddo
    close(lun)
    write(6,*) "[save__results] rslFile is saved...."
    
    return
  end subroutine save__results

  
end module ioUtilityMod
