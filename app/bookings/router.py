from fastapi import APIRouter
from app.bookings.dao import BookingDao
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования']
)


# @router.get('')
# async def get_bookings() -> list[dict[str, SBooking]]:
#     return await BookingDao.find_all()


@router.get('')
async def get_bookings() -> list[SBooking]:
    return await BookingDao.find_all()

