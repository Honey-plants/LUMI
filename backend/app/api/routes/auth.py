from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserRegister, UserLogin, TokenResponse, UserResponse
from app.core.security import hash_password, verify_password, create_access_token, decode_access_token

router = APIRouter(prefix="/auth", tags=["인증"])

# Bearer 토큰 추출기 — Authorization: Bearer <token> 헤더에서 토큰을 꺼냄
bearer_scheme = HTTPBearer()


# ── 회원가입 ───────────────────────────────────────────────────
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(body: UserRegister, db: Session = Depends(get_db)):
    """새 계정을 만든다.

    - username 또는 email이 이미 존재하면 409 에러 반환
    - 비밀번호는 bcrypt로 해싱해서 저장
    """
    # 중복 체크
    if db.query(User).filter(User.username == body.username).first():
        raise HTTPException(status_code=409, detail="이미 사용 중인 아이디입니다.")
    if db.query(User).filter(User.email == body.email).first():
        raise HTTPException(status_code=409, detail="이미 사용 중인 이메일입니다.")

    # 새 유저 생성
    new_user = User(
        username=body.username,
        email=body.email,
        password_hash=hash_password(body.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# ── 로그인 ─────────────────────────────────────────────────────
@router.post("/login", response_model=TokenResponse)
def login(body: UserLogin, db: Session = Depends(get_db)):
    """로그인 후 JWT 액세스 토큰을 발급한다.

    - username이 없거나 비밀번호가 틀리면 401 에러 반환
    - 성공하면 access_token 반환
    """
    user = db.query(User).filter(User.username == body.username).first()

    if not user or not verify_password(body.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="아이디 또는 비밀번호가 올바르지 않습니다.",
        )

    token = create_access_token(data={"sub": user.username})
    return TokenResponse(access_token=token)


# ── 내 정보 조회 ───────────────────────────────────────────────
@router.get("/me", response_model=UserResponse)
def get_me(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
):
    """현재 로그인한 사용자의 정보를 반환한다.

    - Authorization 헤더에 Bearer 토큰이 없거나 유효하지 않으면 401 에러
    """
    username = decode_access_token(credentials.credentials)
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="유효하지 않은 토큰입니다.",
        )

    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")

    return user
