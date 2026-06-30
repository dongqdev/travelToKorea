# Travel To Korea

한국관광공사 오픈 API를 활용해 국내 여행 정보를 조회하고, 회원 기능과 여행 상세 정보를 제공하는 Django 프로젝트입니다.

## 프로젝트 기간

- 2019-07-16 14:38 ~ 2019-07-19 17:25

## 프로젝트 개요

이 프로젝트는 여행지 카테고리, 지역/시군구 선택, 상세 페이지 조회, 회원가입/로그인/마이페이지 기능을 중심으로 구성되어 있습니다. 메인 화면에서는 한국관광공사 API의 지역 정보와 여행 목록을 불러오고, 상세 페이지에서는 선택한 콘텐츠의 이미지와 세부 정보를 보여줍니다.

## 주요 기능

- 메인 페이지에서 지역별 여행 정보 탐색
- 관광지, 문화시설, 축제/공연, 레포츠, 숙박, 쇼핑, 음식점 필터링
- 여행 상세 페이지에서 이미지와 세부 정보 확인
- 회원가입, 로그인, 로그아웃, 마이페이지
- 여행 정보 API 문서 제공 Swagger, Redoc
- REST API 형태의 여행 정보 조회

## 기술 스택

- Backend: Django 2.2.3
- API: Django REST Framework, drf-yasg
- Database: MySQL
- Frontend: Django Template, Vue.js, Vuetify, Axios
- 외부 API: 한국관광공사 Tour API

## 실행 방법

프로젝트를 실행하려면 Python 가상환경과 MySQL 데이터베이스가 필요합니다.

1. 가상환경 활성화 후 의존성 설치

```bash
pip install django djangorestframework drf-yasg mysqlclient
```

2. 데이터베이스 설정 확인

`travel/settings.py`의 `DATABASES` 설정을 현재 MySQL 환경에 맞게 수정합니다.

3. 마이그레이션 실행

```bash
python manage.py makemigrations
python manage.py migrate
```

4. 관리자 계정 생성

```bash
python manage.py createsuperuser
```

5. 개발 서버 실행

```bash
python manage.py runserver
```

6. 브라우저에서 확인

- 메인 페이지: `/maps/`
- 지도/목록 페이지: `/maps/map/`
- 상세 페이지: `/maps/detail/<content_id>/`
- 회원 기능: `/accounts/signup/`, `/accounts/login/`, `/accounts/mypage/<username>/`
- API 문서: `/maps/swagger/`, `/maps/redoc/`

## 프로젝트 구조

```text
travelToKorea/
├─ manage.py
├─ accounts/
│  ├─ views.py
│  ├─ forms.py
│  ├─ urls.py
│  └─ templates/accounts/
├─ maps/
│  ├─ views.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ urls.py
│  └─ templates/maps/
└─ travel/
   ├─ settings.py
   ├─ urls.py
   └─ templates/
```

## 참고 사항

- 메인/상세 페이지는 한국관광공사 오픈 API 응답에 의존합니다.
- `travel/settings.py`와 `maps/views.py` 안에 외부 API 키가 직접 사용되고 있으므로, 배포 전에는 환경 변수로 분리하는 편이 안전합니다.
- 현재 설정은 개발용 `DEBUG = True` 상태입니다.

## 관련 파일

- [프로젝트 설정](travel/settings.py)
- [루트 URL 설정](travel/urls.py)
- [여행 기능 뷰](maps/views.py)
- [회원 기능 뷰](accounts/views.py)