from fastapi import APIRouter, Request, Depends
from app.bookings.dao import BookingDao
from app.bookings.schemas import SBooking
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования']
)


# @router.get('')
# async def get_bookings() -> list[dict[str, SBooking]]:
#     return await BookingDao.find_all()


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)): #-> list[SBooking]
    print(user, type(user), user.id)
    # return await BookingDao.find_all()

