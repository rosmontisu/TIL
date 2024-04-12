from github import Github
import os
import datetime

# 인증
g = Github(os.getenv('GITHUB_TOKEN'))

# 오늘 날짜를 기준으로 경로 및 파일 이름 정의
today = datetime.datetime.now()
year = today.strftime('%Y')
month = today.strftime('%m')
day = today.strftime('%d')

# 한국어 월명 매핑
month_names = {
    '01': '1월', '02': '2월', '03': '3월', '04': '4월',
    '05': '5월', '06': '6월', '07': '7월', '08': '8월',
    '09': '9월', '10': '10월', '11': '11월', '12': '12월'
}

# source_path 설정
source_path = f'TIL/{year}/{month_names[month]}/{year}-{month}-{day}.md'
target_path = f'_posts/{year}-{month}-{day}-til.md'

# 소스에서 파일 내용 가져오기
file_content = source_repo.get_contents(source_path)

# 대상에 파일 업데이트
try:
    # 대상에 파일이 이미 있는지 확인
    existing_file = target_repo.get_contents(target_path)
    target_repo.update_file(target_path, "Update post", file_content.decoded_content.decode(), existing_file.sha)
except:
    target_repo.create_file(target_path, "Create new post", file_content.decoded_content.decode())
