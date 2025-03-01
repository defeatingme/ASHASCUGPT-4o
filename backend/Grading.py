from fastapi import FastAPI, HTTPException, WebSocket
from pydantic import BaseModel
from typing import List, Dict
from enum import Enum
from openai import OpenAI
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
# database.connection import SessionLocal, engine
#from database.models import Base, GPTInteraction
#from models.schemas import GPTRequest, GPTResponse
#from services.openai_service import generate_structured_output
from datetime import datetime

print("imports done!")
client = OpenAI()
app = FastAPI()

print("initializing done!")
