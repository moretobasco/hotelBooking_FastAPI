from fastapi import FastAPI
from app.users.router import router as router_users
from app.bookings.router import router as router_bookings


app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)