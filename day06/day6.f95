program day6
    implicit none
    integer, dimension(300) :: initial
    integer*8 :: ans

    open (1, file = 'input.txt', status = 'old')
    read (1, *) initial
    close(1)

    call reproduce(initial, 80, ans)
    print "(A i13)", "Part 1: ", ans
    call reproduce(initial, 256, ans)
    print "(A i13)", "Part 2: ", ans
    
    contains
    subroutine reproduce(initial, days, total)
        integer, dimension(:), intent(in) :: initial
        integer, intent(in) :: days
        integer*8, intent(out) :: total
        integer*8, dimension(0:8) :: spawns, nextlife
        integer :: i

        spawns = 0
        do i=1,size(initial)
            spawns(initial(i)) = spawns(initial(i)) + 1
        end do
        
        do i=1,days
            nextlife(8) = spawns(0)
            nextlife(0:7) = spawns(1:8)
            nextlife(6) = nextlife(6) + spawns(0)
            spawns = nextlife
        end do
        total = sum(spawns)
    end subroutine
end program day6