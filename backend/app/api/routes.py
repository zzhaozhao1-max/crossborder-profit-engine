from fastapi import APIRouter

router = APIRouter(prefix='/api/v1')

@router.get('/health')
def health():
    return {'status':'ok'}

@router.get('/stores')
def stores():
    return {'stores': []}

@router.get('/profit/dashboard')
def profit_dashboard():
    return {
        'revenue': 0,
        'profit': 0,
        'margin': 0
    }
