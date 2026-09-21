# Django Todo List

Django와 MySQL을 활용하여 구현한 간단한 Todo List 웹 애플리케이션입니다.

짧은 개발 시간 동안 Django의 기본적인 웹 개발 흐름을 익히고,  
로그인/로그아웃부터 회원정보 관리 및 Todo CRUD까지 직접 구현하는 것을 목표로 제작했습니다.

## ⏱️ 개발 기간

- 개발 시간: 약 6시간
- 개발 환경: Windows
- Backend: Django 5.0.3
- Database: MySQL 8.0.46

## 🛠️ 기술 스택

### Backend
- Python
- Django
- MySQL

### Frontend
- HTML
- CSS
- JavaScript

## 📌 주요 기능

### 회원 관리
- 회원가입
- 로그인
- 로그아웃
- 회원정보 조회
- 회원정보 수정
- 회원탈퇴

### Todo List
- Todo 등록
- Todo 조회
- Todo 수정
- Todo 삭제
- Todo 완료 / 미완료 처리
- 시작일 / 종료일 설정
- 종료일까지 24시간 이하로 남은 Todo 표시

### 로그인
- Session을 이용한 로그인 상태 관리
- 로그인한 사용자별 Todo 관리
- 로그아웃 시 Session 초기화

## 🔄 기능 흐름

```text
로그인
  ↓
Todo List
  ├── Todo 등록
  ├── Todo 수정
  ├── Todo 삭제
  └── Todo 완료 처리
  ↓
마이페이지
  ├── 회원정보 수정
  └── 회원탈퇴
  ↓
로그아웃

📝 프로젝트를 통해 학습한 내용
Django에서 URL과 View를 연결하는 방법
Django Template을 이용한 데이터 출력
request.POST를 이용한 데이터 전달
Session을 이용한 로그인 사용자 관리
MySQL과 Django 연결
CRUD 구현 과정
JavaScript를 이용한 POST 요청 처리
사용자별 데이터 접근 제한

