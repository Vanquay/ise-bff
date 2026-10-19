from fastapi import APIRouter, Depends

bookings_router = APIRouter(prefix="/bookings")


@bookings_router.post("/", tags=["bookings"], summary="Create a new booking", 
                      response_model=dict, response_description="Booking details")
async def create_booking():
    return {"message": "Booking created"}

@bookings_router.put("/{booking_id}")
async def update_booking(booking_id: int):
    return {"message": f"Booking {booking_id} updated"}

@bookings_router.delete("/{booking_id}")
async def delete_booking(booking_id: int):
    return {"message": f"Booking {booking_id} deleted"}