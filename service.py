from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )
    res = {
        "users_all": users_all,
    }
    return res


async def get_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "users_one": users_one,
    }
    return res


async def put_users_id(db: Session, id: int, name: str, contact_details: str):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "contact_details": contact_details,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )
    res = {
        "users_edited_record": users_edited_record,
    }
    return res


async def delete_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete
    res = {
        "users_deleted": users_deleted,
    }
    return res


async def get_appointment_types(db: Session):

    query = db.query(models.AppointmentTypes)

    appointment_types_all = query.all()
    appointment_types_all = (
        [new_data.to_dict() for new_data in appointment_types_all]
        if appointment_types_all
        else appointment_types_all
    )
    res = {
        "appointment_types_all": appointment_types_all,
    }
    return res


async def get_appointment_types_id(db: Session, id: int):

    query = db.query(models.AppointmentTypes)
    query = query.filter(and_(models.AppointmentTypes.id == id))

    appointment_types_one = query.first()

    appointment_types_one = (
        (
            appointment_types_one.to_dict()
            if hasattr(appointment_types_one, "to_dict")
            else vars(appointment_types_one)
        )
        if appointment_types_one
        else appointment_types_one
    )

    res = {
        "appointment_types_one": appointment_types_one,
    }
    return res


async def post_appointment_types(db: Session, raw_data: schemas.PostAppointmentTypes):
    id: int = raw_data.id
    name: str = raw_data.name
    duration: int = raw_data.duration

    record_to_be_added = {"id": id, "name": name, "duration": duration}
    new_appointment_types = models.AppointmentTypes(**record_to_be_added)
    db.add(new_appointment_types)
    db.commit()
    db.refresh(new_appointment_types)
    appointment_types_inserted_record = new_appointment_types.to_dict()

    res = {
        "appointment_types_inserted_record": appointment_types_inserted_record,
    }
    return res


async def put_appointment_types_id(db: Session, id: int, name: str, duration: int):

    query = db.query(models.AppointmentTypes)
    query = query.filter(and_(models.AppointmentTypes.id == id))
    appointment_types_edited_record = query.first()

    if appointment_types_edited_record:
        for key, value in {"id": id, "name": name, "duration": duration}.items():
            setattr(appointment_types_edited_record, key, value)

        db.commit()
        db.refresh(appointment_types_edited_record)

        appointment_types_edited_record = (
            appointment_types_edited_record.to_dict()
            if hasattr(appointment_types_edited_record, "to_dict")
            else vars(appointment_types_edited_record)
        )
    res = {
        "appointment_types_edited_record": appointment_types_edited_record,
    }
    return res


async def delete_appointment_types_id(db: Session, id: int):

    query = db.query(models.AppointmentTypes)
    query = query.filter(and_(models.AppointmentTypes.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        appointment_types_deleted = record_to_delete.to_dict()
    else:
        appointment_types_deleted = record_to_delete
    res = {
        "appointment_types_deleted": appointment_types_deleted,
    }
    return res


async def get_appointments(db: Session):

    query = db.query(models.Appointments)

    appointments_all = query.all()
    appointments_all = (
        [new_data.to_dict() for new_data in appointments_all]
        if appointments_all
        else appointments_all
    )
    res = {
        "appointments_all": appointments_all,
    }
    return res


async def get_appointments_id(db: Session, id: int):

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.id == id))

    appointments_one = query.first()

    appointments_one = (
        (
            appointments_one.to_dict()
            if hasattr(appointments_one, "to_dict")
            else vars(appointments_one)
        )
        if appointments_one
        else appointments_one
    )

    res = {
        "appointments_one": appointments_one,
    }
    return res


async def post_appointments(db: Session, raw_data: schemas.PostAppointments):
    id: int = raw_data.id
    date_time: str = raw_data.date_time
    user_id: int = raw_data.user_id
    appointment_type_id: int = raw_data.appointment_type_id

    record_to_be_added = {
        "id": id,
        "user_id": user_id,
        "date_time": date_time,
        "appointment_type_id": appointment_type_id,
    }
    new_appointments = models.Appointments(**record_to_be_added)
    db.add(new_appointments)
    db.commit()
    db.refresh(new_appointments)
    appointments_inserted_record = new_appointments.to_dict()

    res = {
        "appointments_inserted_record": appointments_inserted_record,
    }
    return res


async def put_appointments_id(
    db: Session, id: int, date_time: str, user_id: int, appointment_type_id: int
):

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.id == id))
    appointments_edited_record = query.first()

    if appointments_edited_record:
        for key, value in {
            "id": id,
            "user_id": user_id,
            "date_time": date_time,
            "appointment_type_id": appointment_type_id,
        }.items():
            setattr(appointments_edited_record, key, value)

        db.commit()
        db.refresh(appointments_edited_record)

        appointments_edited_record = (
            appointments_edited_record.to_dict()
            if hasattr(appointments_edited_record, "to_dict")
            else vars(appointments_edited_record)
        )
    res = {
        "appointments_edited_record": appointments_edited_record,
    }
    return res


async def delete_appointments_id(db: Session, id: int):

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        appointments_deleted = record_to_delete.to_dict()
    else:
        appointments_deleted = record_to_delete
    res = {
        "appointments_deleted": appointments_deleted,
    }
    return res


async def get_calendar_events(db: Session):

    query = db.query(models.CalendarEvents)

    calendar_events_all = query.all()
    calendar_events_all = (
        [new_data.to_dict() for new_data in calendar_events_all]
        if calendar_events_all
        else calendar_events_all
    )
    res = {
        "calendar_events_all": calendar_events_all,
    }
    return res


async def get_calendar_events_id(db: Session, id: int):

    query = db.query(models.CalendarEvents)
    query = query.filter(and_(models.CalendarEvents.id == id))

    calendar_events_one = query.first()

    calendar_events_one = (
        (
            calendar_events_one.to_dict()
            if hasattr(calendar_events_one, "to_dict")
            else vars(calendar_events_one)
        )
        if calendar_events_one
        else calendar_events_one
    )

    res = {
        "calendar_events_one": calendar_events_one,
    }
    return res


async def put_calendar_events_id(
    db: Session,
    id: int,
    event_title: str,
    start_time: str,
    end_time: str,
    appointment_id: int,
):

    query = db.query(models.CalendarEvents)
    query = query.filter(and_(models.CalendarEvents.id == id))
    calendar_events_edited_record = query.first()

    if calendar_events_edited_record:
        for key, value in {
            "id": id,
            "end_time": end_time,
            "start_time": start_time,
            "event_title": event_title,
            "appointment_id": appointment_id,
        }.items():
            setattr(calendar_events_edited_record, key, value)

        db.commit()
        db.refresh(calendar_events_edited_record)

        calendar_events_edited_record = (
            calendar_events_edited_record.to_dict()
            if hasattr(calendar_events_edited_record, "to_dict")
            else vars(calendar_events_edited_record)
        )
    res = {
        "calendar_events_edited_record": calendar_events_edited_record,
    }
    return res


async def delete_calendar_events_id(db: Session, id: int):

    query = db.query(models.CalendarEvents)
    query = query.filter(and_(models.CalendarEvents.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        calendar_events_deleted = record_to_delete.to_dict()
    else:
        calendar_events_deleted = record_to_delete
    res = {
        "calendar_events_deleted": calendar_events_deleted,
    }
    return res


async def post_calendar_events(db: Session, document: UploadFile):

    bucket_name = "backstract-testing"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        "s3",
        aws_access_key_id="AKIATET5D5CPSTHVVX25",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1",
    )

    # Read file content
    file_content = await document.read()

    name = document.filename
    file_path = file_path + "/" + name

    import mimetypes

    document.file.seek(0)

    content_type = mimetypes.guess_type(name)[0] or "application/octet-stream"
    s3_client.upload_fileobj(
        document.file, bucket_name, name, ExtraArgs={"ContentType": content_type}
    )

    file_type = Path(document.filename).suffix
    file_size = 200

    file_url = f"https://{bucket_name}.s3.amazonaws.com/{name}"

    doc_file = file_url
    res = {
        "test_file": doc_file,
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    id: int = raw_data.id
    name: str = raw_data.name
    contact_details: str = raw_data.contact_details

    record_to_be_added = {"id": id, "name": name, "contact_details": contact_details}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.id == id))

    user = query.first()

    user = (
        (user.to_dict() if hasattr(user, "to_dict") else vars(user)) if user else user
    )

    res = {
        "users_inserted_record": users_inserted_record,
        "user_student": user,
    }
    return res
