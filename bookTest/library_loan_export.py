import requests
import openpyxl
import time

# 세부주제 코드 목록 (00 ~ 99)
dtl_kdc_list = [f"{i:02d}" for i in range(100)]

# API 기본 정보
auth_key = "a12b0286b0eb37032ee7bbf8f07cbb803f960697da604553b6d0c74140b00287"
url = "http://data4library.kr/api/loanItemSrch"

# 중복 제거용 ISBN 집합
seen_isbns = set()

# 엑셀 워크북 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "통합 도서 정보"

# 헤더 작성
headers = [
    "순번", "순위", "도서명", "저자명", "출판사", "출판년도", "ISBN13",
    "ISBN 부가기호", "권", "주제분류", "주제분류명", "책표지 URL", "도서 상세 URL", "대출건수"
]
ws.append(headers)

# 순회 시작
for dtl_kdc in dtl_kdc_list:
    print(f"📚 {dtl_kdc} 주제 조회 중...")

    params = {
        "authKey": auth_key,
        "dtl_kdc": dtl_kdc,
        "format": "json"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        books = data.get("response", {}).get("docs", [])

        for book in books:
            doc = book.get("doc", {})
            isbn = doc.get("isbn13", "")

            if not isbn or isbn in seen_isbns:
                continue  # 중복 또는 ISBN 없음

            seen_isbns.add(isbn)

            row = [
                doc.get("no", ""),
                doc.get("ranking", ""),
                doc.get("bookname", ""),
                doc.get("authors", ""),
                doc.get("publisher", ""),
                doc.get("publication_year", ""),
                isbn,
                doc.get("addition_symbol", ""),
                doc.get("vol", ""),
                doc.get("class_no", ""),
                doc.get("class_nm", ""),
                doc.get("bookImageURL", ""),
                doc.get("bookDtlUrl", ""),
                doc.get("loan_count", "")
            ]
            ws.append(row)

        time.sleep(1)  # API 요청 간격

    except Exception as e:
        print(f"❌ 오류 발생 ({dtl_kdc}): {e}")

# 엑셀 저장
filename = "도서정보_통합_중복제거.xlsx"
wb.save(filename)
print(f"\n✅ 엑셀 저장 완료: {filename}")
print(f"📦 총 수집된 도서 수: {len(seen_isbns)}권")
