from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import auth

app = FastAPI(
    title="LUMI API",
    description="LUMI의 백엔드 API",
    version="0.1.0",
)

# CORS 설정 — 나중에 React 프론트엔드가 여기 요청을 보낼 수 있게 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite 기본 포트
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(auth.router)


@app.get("/health", tags=["상태 확인"])
def health_check():
    return {"status": "ok", "message": "LUMI 서버가 정상 동작 중입니다"}
