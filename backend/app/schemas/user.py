from pydantic import BaseModel, EmailStr
from datetime import datetime


# ── 회원가입 요청 ──────────────────────────────────────────────
class UserRegister(BaseModel):
    username: str
    email: EmailStr       # 이메일 형식 자동 검증
    password: str


# ── 로그인 요청 ────────────────────────────────────────────────
class UserLogin(BaseModel):
    username: str
    password: str


# ── 토큰 응답 (로그인 성공 시 반환) ───────────────────────────
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ── 내 정보 응답 (/auth/me) ────────────────────────────────────
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    model_config = {"from_attributes": True}  # SQLAlchemy 모델 → Pydantic 자동 변환
