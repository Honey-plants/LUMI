# 🌙 LUMI — 포트폴리오 4주 개발 계획서

> **목표:** 한 달 안에 GitHub에 올릴 수 있는 완성도 높은 풀스택 프로젝트 완성  
> **투자 시간:** 하루 5시간 이상  
> **기술 수준:** Python · React · SQL 기초 보유

---

## 📌 기술 스택

| 영역 | 기술 | 이유 |
|------|------|------|
| 백엔드 | Python + FastAPI | 빠르고 문서 자동 생성, 포트폴리오에 잘 보임 |
| 프론트엔드 | React + Vite | 현업 표준, 기초 있으면 빠르게 진행 가능 |
| 데이터베이스 | SQLite → PostgreSQL | SQLite로 빠르게 시작, 완성 후 PostgreSQL로 업그레이드 |
| 인증 | JWT (JSON Web Token) | 실무에서 가장 많이 쓰는 인증 방식 |
| AI 연동 | Ollama (로컬 LLM) | 인터넷 없이 무료로 AI 기능 구현 가능 |
| 버전 관리 | Git + GitHub | 포트폴리오 필수 |

---

## 🗓️ 주차별 계획

---

### 1주차 (Day 1~7) — 프로젝트 기반 구축

**목표:** 로그인/회원가입이 되는 백엔드 API 완성

#### Day 1~2: 환경 설정 & 프로젝트 구조 잡기
- [ ] Git 저장소 생성 (GitHub에 LUMI 레포 만들기)
- [ ] 폴더 구조 설계
  ```
  LUMI/
  ├── backend/        ← FastAPI 서버
  ├── frontend/       ← React 앱
  └── README.md
  ```
- [ ] Python 가상환경 설정 (`venv`)
- [ ] FastAPI, SQLAlchemy, python-jose 등 패키지 설치

#### Day 3~4: 데이터베이스 모델 설계
- [ ] SQLite 연결 설정
- [ ] User 테이블 모델 작성 (id, username, email, password_hash, created_at)
- [ ] Alembic으로 마이그레이션 설정

#### Day 5~6: 회원가입 / 로그인 API 구현
- [ ] POST `/auth/register` — 회원가입
- [ ] POST `/auth/login` — 로그인 + JWT 토큰 발급
- [ ] GET `/auth/me` — 내 정보 조회 (토큰 인증 필요)
- [ ] 비밀번호 bcrypt 해싱 적용

#### Day 7: 테스트 & 첫 커밋
- [ ] Postman 또는 FastAPI 자동 문서(`/docs`)로 API 테스트
- [ ] GitHub에 1주차 코드 커밋 & 푸시
- [ ] 커밋 메시지 규칙 정하기 (예: `feat: 로그인 API 구현`)

---

### 2주차 (Day 8~14) — 핵심 기능 백엔드

**목표:** 할 일 · 목표 · 루틴 관리 API 완성

#### Day 8~9: 할 일(Todo) CRUD
- [ ] Todo 테이블 모델 작성 (id, user_id, title, content, is_done, due_date)
- [ ] GET `/todos` — 목록 조회
- [ ] POST `/todos` — 생성
- [ ] PATCH `/todos/{id}` — 수정 / 완료 처리
- [ ] DELETE `/todos/{id}` — 삭제

#### Day 10~11: 목표(Goal) 관리
- [ ] Goal 테이블 모델 작성 (id, user_id, title, description, deadline, progress)
- [ ] 목표 CRUD API 구현
- [ ] 목표 진행률 계산 로직 (완료된 Todo 비율로 계산)

#### Day 12~13: 루틴(Routine) 관리
- [ ] Routine 테이블 모델 작성 (id, user_id, title, frequency, last_done_at)
- [ ] 루틴 CRUD API 구현
- [ ] 루틴 체크 API 구현 (오늘 루틴 완료 처리)

#### Day 14: 정리 & 커밋
- [ ] 전체 API 연결 테스트
- [ ] 에러 처리 보완 (없는 항목 조회 시 404 반환 등)
- [ ] GitHub 2주차 커밋

---

### 3주차 (Day 15~21) — React 프론트엔드

**목표:** 백엔드와 연결된 실제 화면 완성

#### Day 15~16: React 프로젝트 설정
- [ ] Vite로 React 프로젝트 생성
- [ ] React Router 설치 및 라우팅 설정
  - `/login`, `/register`, `/dashboard`, `/todos`, `/goals`, `/routines`
- [ ] Axios 설치 (API 호출용)
- [ ] 전역 상태 관리 (Context API 또는 Zustand)

#### Day 17~18: 로그인 / 회원가입 화면
- [ ] 로그인 페이지 UI 구현
- [ ] 회원가입 페이지 UI 구현
- [ ] JWT 토큰 저장 및 자동 로그인 처리
- [ ] 로그인 안 한 상태에서 보호된 페이지 접근 차단

#### Day 19~20: 핵심 기능 화면
- [ ] 대시보드 — 오늘 할 일, 목표 현황, 루틴 요약
- [ ] 할 일 관리 화면 (추가 / 완료 / 삭제)
- [ ] 목표 관리 화면 (진행률 표시)
- [ ] 루틴 체크 화면

#### Day 21: 연결 테스트 & 커밋
- [ ] 백엔드 API와 프론트엔드 전체 연결 확인
- [ ] 기본 스타일링 (CSS / Tailwind 선택)
- [ ] GitHub 3주차 커밋

---

### 4주차 (Day 22~28) — AI 기능 + 포트폴리오 완성

**목표:** AI 코칭 기능 추가 + GitHub 포트폴리오 완성

#### Day 22~23: Ollama AI 연동
- [ ] Ollama 설치 및 모델 다운로드 (추천: `llama3.2` 또는 `gemma2`)
- [ ] FastAPI에서 Ollama API 호출 엔드포인트 구현
  - POST `/ai/coach` — 오늘의 할 일/목표 기반 AI 피드백 요청
- [ ] React에서 AI 채팅 화면 구현

#### Day 24~25: AI 기능 고도화
- [ ] 사용자 데이터(할 일, 목표, 루틴)를 AI 프롬프트에 반영
- [ ] "오늘 어떻게 시작할까요?" 타입의 동기부여 메시지 생성
- [ ] AI 응답 스트리밍 (타이핑 효과)

#### Day 26~27: GitHub README 작성
- [ ] README.md 구성
  - 프로젝트 소개 및 주요 기능
  - 기술 스택 배지
  - 실행 방법 (로컬 설치 가이드)
  - 주요 화면 스크린샷
  - API 문서 링크
- [ ] `.env.example` 파일 작성 (환경변수 예시)
- [ ] `.gitignore` 점검 (secret key, DB 파일 등 제외)

#### Day 28: 최종 점검 & 완성
- [ ] 전체 기능 흐름 테스트 (회원가입 → 로그인 → 할 일 추가 → AI 피드백)
- [ ] 코드 주석 정리
- [ ] 최종 GitHub 푸시
- [ ] LinkedIn / 노션 포트폴리오에 LUMI 추가

---

## 📊 완성 후 포트폴리오에서 강조할 포인트

| 강조 포인트 | 내용 |
|------------|------|
| **풀스택 구현** | 백엔드(FastAPI) + 프론트엔드(React) 직접 연결 |
| **JWT 인증** | 실무에서 쓰는 토큰 기반 인증 직접 구현 |
| **REST API 설계** | 일관된 엔드포인트 구조와 에러 처리 |
| **AI 연동** | Ollama 로컬 LLM을 활용한 AI 코칭 기능 |
| **데이터베이스 설계** | 관계형 모델 (사용자 ↔ 할 일 ↔ 목표 ↔ 루틴) |

---

## ⚠️ 막혔을 때 대처법

- **모르는 개념이 나왔을 때** → 그 부분만 따로 검색하거나 AI한테 물어보기. 전체를 다시 공부하려 하지 말기
- **기능이 너무 복잡할 때** → 더 단순하게 줄이기. 완성이 완벽보다 중요
- **진도가 느릴 때** → AI 기능은 4주차에 있으니 3주차까지만 완성해도 포트폴리오로 충분

---

## 📁 GitHub 커밋 전략

```
feat: 새로운 기능 추가
fix: 버그 수정
refactor: 코드 개선 (기능 변화 없음)
docs: README 등 문서 작성
style: UI 스타일 변경
```

> 매일 최소 1회 커밋 → GitHub 잔디 채우기 = 성실함의 증거

---

*계획은 시작점입니다. 진행하면서 조정해도 됩니다.* 🚀
