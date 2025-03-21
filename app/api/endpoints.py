from fastapi import APIRouter, Request, HTTPException, responses
from app import config
import logging
from datetime import datetime

router = APIRouter()

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

@router.post("/calculate_bonus")
async def calculate_bonus(request: Request):
    '''Рассчитывает бонусы с каждой покупки'''
    try:
        data = await request.json()
        transaction_amount = data['transaction_amount'] # сумма покупки
        timestamp_str = data['timestamp'] # дата покупки
        customer_status = data['customer_status']

        timestamp = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
        weekday = timestamp.isoweekday()

        applied_rules = []
        base_bonus = transaction_amount / config.config['BASE_RATE'] # базовое правило
        applied_rules.append({'rule': 'base_rate', 'bonus': base_bonus})
        total_bonus = base_bonus

        if weekday in [6, 7]:
            holiday_bonus = base_bonus * config.config['HOLIDAY_BONUS']
            applied_rules.append({'rule': 'holiday_bonus', 'bonus': holiday_bonus})
            total_bonus += holiday_bonus
        if customer_status == 'vip':
            vip_bonus = total_bonus * config.config['VIP_BONUS']
            applied_rules.append({'rule': 'holiday_bonus', 'bonus': vip_bonus})

        log.info(' [x] Successfull: calculate_bonus')
        return responses.JSONResponse({'total_bonus': total_bonus, 'applied_rules': applied_rules})

    except KeyError as e:
        raise HTTPException(status_code=400, detail=f'Missing required field: {e}')
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f'Invalid data format: {e}')




