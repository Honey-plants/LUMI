from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# DB 엔진 생성 — settings에서 DATABASE_URL 읽어옴
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLite 전용 설정
)

# 세션 팩토리 — DB와 대화할 때마다 세션 하나씩 열고 닫음
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모든 모델 클래스가 상속받을 베이스 클래스
Base = declarative_base()

# 의존성 주입용 함수 — FastAPI 엔드포인트에서 DB 세션을 받아쓸 때 사용
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()