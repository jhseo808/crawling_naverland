import requests
import json
from datetime import datetime

cookies = {
    'NNB': '4V56TAX3NWDWM',
    'ASID': 'd32083b200000190b4da521600000056',
    '_ga': 'GA1.1.1371603422.1725523153',
    'm_loc': 'a623afb3d1d7f05cdf707a5d56ea35ced8ab6dcb02754f967317ee047437eb2a',
    'NV_WETR_LAST_ACCESS_RGN_M': '"MDk1NjA1NDA="',
    'NV_WETR_LOCATION_RGN_M': '"MDk1NjA1NDA="',
    'NSCS': '2',
    '_ga_451MFZ9CFM': 'GS1.1.1736725422.2.1.1736725743.0.0.0',
    '_fbp': 'fb.1.1736901231587.700769679592911950',
    '_gcl_au': '1.1.2109888356.1736901232',
    'naverfinancial_CID': '351c3df6ef4f493cafc4e8413b52c072',
    '_tt_enable_cookie': '1',
    '_ttp': 'KjSjKsOcniAX5x6fQIE4yWeeCA8.tt.1',
    '_fwb': '612yL5qTPFVL56m9qmywVW.1740525530381',
    '_ga_8P4PY65YZ2': 'GS1.1.1741753594.1.1.1741753600.54.0.0',
    '_ga_NFRXYYY5S0': 'GS1.1.1741824003.1.1.1741824071.0.0.0',
    '_ga_9JHCQLWL5X': 'GS1.1.1741824003.1.1.1741824071.0.0.0',
    '_ga_Q7G1QTKPGB': 'GS1.1.1741824003.2.1.1741824071.0.0.0',
    'NAC': 'WUNiBgQ5T5va',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    '_fwb': '612yL5qTPFVL56m9qmywVW.1740525530381',
    'landHomeFlashUseYn': 'Y',
    'realestate.beta.lastclick.cortar': '4100000000',
    'NACT': '1',
    'nid_inf': '1903230816',
    'NID_AUT': 'YX7KTkcgjU6QVpZ5T/9rDU2KPrZvSRMGeTUQqK/nT9eUzpEVIMqVQ6zeTVoy1420',
    'NID_JKL': 'UtP1qks/NXZph25hpTiSxbE1S4sqUoyyh0tEDHj9bPA=',
    'page_uid': 'i+5ApwpzL8VssjeXiFNssssssK0-420205',
    'SRT30': '1742892536',
    'NID_SES': 'AAAB2ReQDEeD3BWscoZr4VVvslDu7+vs5UfBsgmByiyvoGyxL5YSH8V5N0HQK3nCmY8GVBgNK43/ZRSnxQIHBVuqgHLGjheQ6Ofi07l9EcufLLHzgvhgweq8GhGVYCLrR3IZdO8Va0Km3cGJqRRlANV3IEYKSa8Z18rmF6CpyWZRxG6zJy7C5N94GQ94UsqLPm3XfZUY0kgZ8+pdx3tDwoKGRYHJI3qxHclvBO3uSDyZ0ZKfbhTRe7BI4I1iid6OeL0PUPE7oXwRksmfdY/bGn5TIpBB+pvg/fczT17XoMjobQu1jIhmBw3YnW2RrwcwFzgkAt2CqICl1K/QJ1Ytza1c0OQZA9UuAHpAzfKb+B8oZD0JMSHkahPivkPDJM2269ibfTKeqTZnLGyh44At0zehOkA8RLclZ3Rx2fXpgfggemD+i6mIL8HyqcI06ZnHDcuLAz4ItyHmgayfN+zS/RYb00ybgdjbveskGCQSWR7iFQF4T9f6Z1rY3fYFMvv1xdPHsyb1JoV7OUyI0xar6fUTJOcD0E6pujEy2YIS38YvcAcJ6oO1XIRMSdTaOm8hmvvJEeQDlxn16+dwjXhEMd81vUHMHqp4jjLv9YoY8IYUi0+AEZdILZ3z1ePMDuhouMfwsw==',
    'SRT5': '1742893391',
    'REALESTATE': 'Tue%20Mar%2025%202025%2018%3A03%3A13%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'BUC': '6F1-CYdJmmCZxEsN4YqdqMyZKs1eTxft2yDDPk0sn7g=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDI4OTMzOTMsImV4cCI6MTc0MjkwNDE5M30.2nU-O2d4sO6eeJjS_r6HgbZ3pZnilFWC0LGSsZAujBk',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/2890?ms=37.3580552,126.9448134,16&a=APT:PRE:ABYG:JGC&b=A1&e=RETAIL',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    # 'cookie': 'NNB=4V56TAX3NWDWM; ASID=d32083b200000190b4da521600000056; _ga=GA1.1.1371603422.1725523153; m_loc=a623afb3d1d7f05cdf707a5d56ea35ced8ab6dcb02754f967317ee047437eb2a; NV_WETR_LAST_ACCESS_RGN_M="MDk1NjA1NDA="; NV_WETR_LOCATION_RGN_M="MDk1NjA1NDA="; NSCS=2; _ga_451MFZ9CFM=GS1.1.1736725422.2.1.1736725743.0.0.0; _fbp=fb.1.1736901231587.700769679592911950; _gcl_au=1.1.2109888356.1736901232; naverfinancial_CID=351c3df6ef4f493cafc4e8413b52c072; _tt_enable_cookie=1; _ttp=KjSjKsOcniAX5x6fQIE4yWeeCA8.tt.1; _fwb=612yL5qTPFVL56m9qmywVW.1740525530381; _ga_8P4PY65YZ2=GS1.1.1741753594.1.1.1741753600.54.0.0; _ga_NFRXYYY5S0=GS1.1.1741824003.1.1.1741824071.0.0.0; _ga_9JHCQLWL5X=GS1.1.1741824003.1.1.1741824071.0.0.0; _ga_Q7G1QTKPGB=GS1.1.1741824003.2.1.1741824071.0.0.0; NAC=WUNiBgQ5T5va; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; _fwb=612yL5qTPFVL56m9qmywVW.1740525530381; landHomeFlashUseYn=Y; realestate.beta.lastclick.cortar=4100000000; NACT=1; nid_inf=1903230816; NID_AUT=YX7KTkcgjU6QVpZ5T/9rDU2KPrZvSRMGeTUQqK/nT9eUzpEVIMqVQ6zeTVoy1420; NID_JKL=UtP1qks/NXZph25hpTiSxbE1S4sqUoyyh0tEDHj9bPA=; page_uid=i+5ApwpzL8VssjeXiFNssssssK0-420205; SRT30=1742892536; NID_SES=AAAB2ReQDEeD3BWscoZr4VVvslDu7+vs5UfBsgmByiyvoGyxL5YSH8V5N0HQK3nCmY8GVBgNK43/ZRSnxQIHBVuqgHLGjheQ6Ofi07l9EcufLLHzgvhgweq8GhGVYCLrR3IZdO8Va0Km3cGJqRRlANV3IEYKSa8Z18rmF6CpyWZRxG6zJy7C5N94GQ94UsqLPm3XfZUY0kgZ8+pdx3tDwoKGRYHJI3qxHclvBO3uSDyZ0ZKfbhTRe7BI4I1iid6OeL0PUPE7oXwRksmfdY/bGn5TIpBB+pvg/fczT17XoMjobQu1jIhmBw3YnW2RrwcwFzgkAt2CqICl1K/QJ1Ytza1c0OQZA9UuAHpAzfKb+B8oZD0JMSHkahPivkPDJM2269ibfTKeqTZnLGyh44At0zehOkA8RLclZ3Rx2fXpgfggemD+i6mIL8HyqcI06ZnHDcuLAz4ItyHmgayfN+zS/RYb00ybgdjbveskGCQSWR7iFQF4T9f6Z1rY3fYFMvv1xdPHsyb1JoV7OUyI0xar6fUTJOcD0E6pujEy2YIS38YvcAcJ6oO1XIRMSdTaOm8hmvvJEeQDlxn16+dwjXhEMd81vUHMHqp4jjLv9YoY8IYUi0+AEZdILZ3z1ePMDuhouMfwsw==; SRT5=1742893391; REALESTATE=Tue%20Mar%2025%202025%2018%3A03%3A13%20GMT%2B0900%20(Korean%20Standard%20Time); BUC=6F1-CYdJmmCZxEsN4YqdqMyZKs1eTxft2yDDPk0sn7g=',
}

response = requests.get(
    'https://new.land.naver.com/api/articles/complex/2890?realEstateType=APT%3APRE%3AABYG%3AJGC&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page=2&complexNo=2890&buildingNos=&areaNos=&type=list&order=rank',
    cookies=cookies,
    headers=headers,
)

# 현재 시간을 파일명에 포함
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f'naver_land_{current_time}.json'

# JSON 형식으로 저장
if response.status_code == 200:
    try:
        data = response.json()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f'데이터가 {filename}에 저장되었습니다.')
    except Exception as e:
        print(f'데이터 저장 중 오류 발생: {str(e)}')
else:
    print(f'API 요청 실패: {response.status_code}')
