# JUN'S TOUR — Mobile Brochures

준스투어 여행 일정 모바일 브로슈어입니다. 별도 앱·프로그램 설치 없이 카카오톡으로 링크를 보내면
고객님 휴대폰에서 바로 열립니다. GitHub Pages로 서비스됩니다.

## 주소

| 페이지 | 주소 |
| --- | --- |
| 브로슈어 목록 | https://dandy914-collab.github.io/JUNS-TOUT-/ |
| 라오스 비엔티안·방비엥 (2027.01.18–22) | https://dandy914-collab.github.io/JUNS-TOUT-/laos-2027-01/ |

## 구성

```
index.html                     브로슈어 목록(허브) — 새 행사는 여기에 카드 추가
laos-2027-01/
  index.html                   라오스 브로슈어 본문 (한 파일에 스타일 포함)
  assets/og.jpg                카카오톡 링크 미리보기 썸네일 (1200×630)
  assets/logo_*.png            준스투어 로고 (흰색/네이비/골드)
  assets/img/*.jpg             본문 사진 14장 (웹 최적화)
tools/build_assets.py          사진 리사이즈·크롭 스크립트 (워크스페이스 원본에서 생성)
```

## 내용 수정 방법

- **문구·일정·가격**: `laos-2027-01/index.html`의 해당 부분을 고치고 커밋·푸시하면 1~2분 뒤 링크에 반영됩니다.
  링크 주소는 그대로이므로 이미 보낸 카톡 링크도 자동으로 최신 내용을 보여줍니다.
- **사진 교체**: 원본 사진을 `tools/build_assets.py` 기준 경로에 두고 스크립트를 실행해 `assets/img/`를 다시 만듭니다.
- **새 행사 추가**: `laos-2027-01/` 폴더를 복사해 이름을 바꾸고(예: `kotakinabalu-2027-02/`) `index.html`의
  og:url·og:image·canonical을 새 주소로 바꾼 뒤, 허브 `index.html`에 카드를 하나 더 추가합니다.

## 카카오톡 공유

링크를 붙여넣으면 `og:title` / `og:description` / `og:image` 기준으로 썸네일 카드가 뜹니다.
(카카오는 한 번 읽은 미리보기를 캐시하므로, 문구를 바꾼 뒤에는
[카카오 디벨로퍼스 OG 캐시 삭제](https://developers.kakao.com/tool/clear/og)에서 주소를 넣고 초기화하면 즉시 반영됩니다.)

## 사진 출처

Basile Morin · Christophe95 · Wikimedia Commons (CC BY-SA 4.0)
