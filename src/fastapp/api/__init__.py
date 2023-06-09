from fastapi import APIRouter
from .operations import router as operations_router
from .reports import router as reports_router
router = APIRouter()

router.include_router(operations_router)
router.include_router(reports_router)
