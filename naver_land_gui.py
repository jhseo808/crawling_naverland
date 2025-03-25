import sys
import json
import requests
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QLineEdit, 
                             QTableWidget, QTableWidgetItem, QComboBox, 
                             QMessageBox, QSpinBox)
from PySide6.QtCore import Qt

class NaverLandApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("네이버 부동산 매물 검색")
        self.setGeometry(100, 100, 1200, 800)
        
        # 메인 위젯 설정
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # 검색 조건 위젯
        search_widget = QWidget()
        search_layout = QHBoxLayout(search_widget)
        
        # 단지번호 입력
        self.complex_no = QLineEdit()
        self.complex_no.setPlaceholderText("단지번호")
        self.complex_no.setText("2890")  # 기본값 설정
        
        # 거래유형 선택
        self.trade_type = QComboBox()
        self.trade_type.addItems(["매매", "전세", "월세"])
        
        # 가격 범위 설정
        self.price_min = QSpinBox()
        self.price_min.setRange(0, 1000000)
        self.price_min.setSuffix("만원")
        
        self.price_max = QSpinBox()
        self.price_max.setRange(0, 1000000)
        self.price_max.setValue(90000)  # 9억원 기본값
        self.price_max.setSuffix("만원")
        
        # 검색 버튼
        search_btn = QPushButton("검색")
        search_btn.clicked.connect(self.search_properties)
        
        # 저장 버튼
        save_btn = QPushButton("JSON 저장")
        save_btn.clicked.connect(self.save_to_json)
        
        # 검색 조건 위젯에 컴포넌트 추가
        search_layout.addWidget(QLabel("단지번호:"))
        search_layout.addWidget(self.complex_no)
        search_layout.addWidget(QLabel("거래유형:"))
        search_layout.addWidget(self.trade_type)
        search_layout.addWidget(QLabel("최소가격:"))
        search_layout.addWidget(self.price_min)
        search_layout.addWidget(QLabel("최대가격:"))
        search_layout.addWidget(self.price_max)
        search_layout.addWidget(search_btn)
        search_layout.addWidget(save_btn)
        
        # 테이블 위젯 설정
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "매물번호", "거래유형", "가격", "면적", "층", "방향", "확인일"
        ])
        
        # 레이아웃에 위젯 추가
        layout.addWidget(search_widget)
        layout.addWidget(self.table)
        
        self.current_data = None  # 현재 검색된 데이터 저장용
        
    def search_properties(self):
        complex_no = self.complex_no.text()
        trade_type = "A1" if self.trade_type.currentText() == "매매" else "B1"
        price_min = self.price_min.value() * 10000  # 만원 -> 원
        price_max = self.price_max.value() * 10000
        
        # 최신 쿠키 값으로 업데이트
        cookies = {
            'NNB': '4V56TAX3NWDWM',
            'ASID': 'd32083b200000190b4da521600000056',
            'm_loc': 'a623afb3d1d7f05cdf707a5d56ea35ced8ab6dcb02754f967317ee047437eb2a',
            'NV_WETR_LAST_ACCESS_RGN_M': '"MDk1NjA1NDA="',
            'NV_WETR_LOCATION_RGN_M': '"MDk1NjA1NDA="',
            'NSCS': '2',
            'REALESTATE': 'Tue%20Mar%2025%202025%2018%3A03%3A13%20GMT%2B0900%20(Korean%20Standard%20Time)',
            'NID_AUT': 'YX7KTkcgjU6QVpZ5T/9rDU2KPrZvSRMGeTUQqK/nT9eUzpEVIMqVQ6zeTVoy1420',
            'NID_JKL': 'UtP1qks/NXZph25hpTiSxbE1S4sqUoyyh0tEDHj9bPA=',
            'NID_SES': 'AAAB2ReQDEeD3BWscoZr4VVvslDu7+vs5UfBsgmByiyvoGyxL5YSH8V5N0HQK3nCmY8GVBgNK43/ZRSnxQIHBVuqgHLGjheQ6Ofi07l9EcufLLHzgvhgweq8GhGVYCLrR3IZdO8Va0Km3cGJqRRlANV3IEYKSa8Z18rmF6CpyWZRxG6zJy7C5N94GQ94UsqLPm3XfZUY0kgZ8+pdx3tDwoKGRYHJI3qxHclvBO3uSDyZ0ZKfbhTRe7BI4I1iid6OeL0PUPE7oXwRksmfdY/bGn5TIpBB+pvg/fczT17XoMjobQu1jIhmBw3YnW2RrwcwFzgkAt2CqICl1K/QJ1Ytza1c0OQZA9UuAHpAzfKb+B8oZD0JMSHkahPivkPDJM2269ibfTKeqTZnLGyh44At0zehOkA8RLclZ3Rx2fXpgfggemD+i6mIL8HyqcI06ZnHDcuLAz4ItyHmgayfN+zS/RYb00ybgdjbveskGCQSWR7iFQF4T9f6Z1rY3fYFMvv1xdPHsyb1JoV7OUyI0xar6fUTJOcD0E6pujEy2YIS38YvcAcJ6oO1XIRMSdTaOm8hmvvJEeQDlxn16+dwjXhEMd81vUHMHqp4jjLv9YoY8IYUi0+AEZdILZ3z1ePMDuhouMfwsw==',
            'SRT5': '1742893391',
            'BUC': '6F1-CYdJmmCZxEsN4YqdqMyZKs1eTxft2yDDPk0sn7g=',
        }

        headers = {
            'accept': '*/*',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDI4OTMzOTMsImV4cCI6MTc0MjkwNDE5M30.2nU-O2d4sO6eeJjS_r6HgbZ3pZnilFWC0LGSsZAujBk',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
            'referer': 'https://new.land.naver.com/',
            'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
        }
        
        url = f'https://new.land.naver.com/api/articles/complex/{complex_no}'
        params = {
            'realEstateType': 'APT:PRE:ABYG:JGC',
            'tradeType': trade_type,
            'tag': '::::::::',
            'rentPriceMin': 0,
            'rentPriceMax': 900000000,
            'priceMin': price_min,
            'priceMax': price_max,
            'areaMin': 0,
            'areaMax': 900000000,
            'priceType': 'RETAIL',
            'page': 1,
            'complexNo': complex_no,
            'type': 'list',
            'order': 'rank'
        }
        
        try:
            # 세션 생성
            session = requests.Session()
            
            # 먼저 메인 페이지 방문
            session.get('https://new.land.naver.com/', headers=headers, cookies=cookies)
            
            # API 요청
            response = session.get(url, params=params, headers=headers, cookies=cookies)
            
            if response.status_code == 200:
                data = response.json()
                self.current_data = data
                self.update_table(data)
            else:
                error_msg = f"API 요청 실패: {response.status_code}\n"
                error_msg += f"응답 내용: {response.text}"
                QMessageBox.warning(self, "오류", error_msg)
        except Exception as e:
            QMessageBox.warning(self, "오류", f"데이터 조회 중 오류 발생: {str(e)}")
    
    def update_table(self, data):
        if 'articleList' not in data:
            QMessageBox.warning(self, "알림", "검색 결과가 없습니다.")
            return
            
        articles = data['articleList']
        self.table.setRowCount(len(articles))
        
        for row, article in enumerate(articles):
            self.table.setItem(row, 0, QTableWidgetItem(str(article.get('articleNo', ''))))
            self.table.setItem(row, 1, QTableWidgetItem(article.get('tradeTypeName', '')))
            self.table.setItem(row, 2, QTableWidgetItem(f"{article.get('price', '')}만원"))
            self.table.setItem(row, 3, QTableWidgetItem(f"{article.get('area', '')}㎡"))
            self.table.setItem(row, 4, QTableWidgetItem(f"{article.get('floor', '')}층"))
            self.table.setItem(row, 5, QTableWidgetItem(article.get('direction', '')))
            self.table.setItem(row, 6, QTableWidgetItem(article.get('confirmYmd', '')))
        
        self.table.resizeColumnsToContents()
    
    def save_to_json(self):
        if not self.current_data:
            QMessageBox.warning(self, "알림", "저장할 데이터가 없습니다. 먼저 검색을 실행해주세요.")
            return
            
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'naver_land_{current_time}.json'
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.current_data, f, ensure_ascii=False, indent=2)
            QMessageBox.information(self, "성공", f"데이터가 {filename}에 저장되었습니다.")
        except Exception as e:
            QMessageBox.warning(self, "오류", f"파일 저장 중 오류 발생: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NaverLandApp()
    window.show()
    sys.exit(app.exec()) 
