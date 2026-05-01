import bcrypt
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt

from app.core.config import settings


# ── 비밀번호 관련 ──────────────────────────────────────────────

def hash_password(plain_password: str) -> str:
    """평문 비밀번호를 bcrypt 해시로 변환"""
    return bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """입력한 비밀번호가 저장된 해시와 일치하는지 확인"""
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


# ── JWT 토큰 관련 ──────────────────────────────────────────────

def create_access_token(data: dict) -> str:
    """JWT 액세스 토큰 생성

    - data: 토큰 안에 담을 정보 (보통 {"sub": username})
    - 만료 시간은 settings.ACCESS_TOKEN_EXPIRE_MINUTES 기준
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_access_token(token: str) -> str | None:
    """JWT 토큰을 해석해서 username(sub) 반환

    - 유효하지 않거나 만료된 토큰이면 None 반환
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        return username
    except JWTError:
        return None
