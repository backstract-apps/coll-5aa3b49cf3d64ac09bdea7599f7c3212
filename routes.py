from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(id: int, name: str, contact_details: str, db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, id, name, contact_details)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointment_types/')
async def get_appointment_types(db: Session = Depends(get_db)):
    try:
        return await service.get_appointment_types(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointment_types/id')
async def get_appointment_types_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_appointment_types_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/appointment_types/')
async def post_appointment_types(raw_data: schemas.PostAppointmentTypes, db: Session = Depends(get_db)):
    try:
        return await service.post_appointment_types(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/appointment_types/id/')
async def put_appointment_types_id(id: int, name: str, duration: int, db: Session = Depends(get_db)):
    try:
        return await service.put_appointment_types_id(db, id, name, duration)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/appointment_types/id')
async def delete_appointment_types_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_appointment_types_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointments/')
async def get_appointments(db: Session = Depends(get_db)):
    try:
        return await service.get_appointments(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointments/id')
async def get_appointments_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_appointments_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/appointments/')
async def post_appointments(raw_data: schemas.PostAppointments, db: Session = Depends(get_db)):
    try:
        return await service.post_appointments(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/appointments/id/')
async def put_appointments_id(id: int, date_time: str, user_id: int, appointment_type_id: int, db: Session = Depends(get_db)):
    try:
        return await service.put_appointments_id(db, id, date_time, user_id, appointment_type_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/appointments/id')
async def delete_appointments_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_appointments_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/calendar_events/')
async def get_calendar_events(db: Session = Depends(get_db)):
    try:
        return await service.get_calendar_events(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/calendar_events/id')
async def get_calendar_events_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_calendar_events_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/calendar_events/id/')
async def put_calendar_events_id(id: int, event_title: str, start_time: str, end_time: str, appointment_id: int, db: Session = Depends(get_db)):
    try:
        return await service.put_calendar_events_id(db, id, event_title, start_time, end_time, appointment_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/calendar_events/id')
async def delete_calendar_events_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_calendar_events_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/calendar_events/')
async def post_calendar_events(document: UploadFile, db: Session = Depends(get_db)):
    try:
        return await service.post_calendar_events(db, document)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

