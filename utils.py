
from app.common.database import DBScore
from datetime import datetime

import hashlib
import config
import os

def setup():
    if not config.S3_ENABLED:
        # Create required folders if not they not already exist
        os.makedirs(f'{config.DATA_PATH}/images/achievements', exist_ok=True)
        os.makedirs(f'{config.DATA_PATH}/screenshots', exist_ok=True)
        os.makedirs(f'{config.DATA_PATH}/replays', exist_ok=True)
        os.makedirs(f'{config.DATA_PATH}/avatars', exist_ok=True)

def compute_score_checksum(score: DBScore) -> str:
    return hashlib.md5(
        f'{score.n100 + score.n300}p{score.n50}o{score.nGeki}o{score.nKatu}t{score.nMiss}a{score.beatmap.md5}r{score.max_combo}e{score.perfect}y{score.user.name}o{score.total_score}u{score.grade}{score.mods}{not score.failtime}'.encode()
    ).hexdigest()

def get_ticks(dt) -> int:
    dt = dt.replace(tzinfo=None)
    return int((dt - datetime(1, 1, 1)).total_seconds() * 10000000)
