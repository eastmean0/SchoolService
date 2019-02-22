#-*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import strftime
import smtplib
from email.message import EmailMessage
import re



def main():
	print("경일고등학교 카카오 학생 서비스 입니다.")
	print("번호를 선택해주세요.")
	print("------------------------------------\n")
	print("[1] 급식 매뉴 보기")
	print("[2] 경일 신문고")
	choice = int(input())

	if choice == 1:
		schoolfood()
		notice()
	elif choice == 2:
		report()
		notice()
		
	else:
		print("아직 지원하지 않는 서비스 입니다.")
		main()


def schoolfood(): 
	print("경일고 급식봇입니다.")
	print("금주의 급식을 보려면 ""금주 급식"" 이라고 입력해주세요.")
	a = str(input())

	if a == "금주 급식":

		print("조식[1] 중식[2] 석식[3]")
		meal = int(input())

		if meal >= 4:
			print("선택 항목에 없습니다")
		else:
			print("%s번 옵션을 선택했습니다." %(meal))

		Year = strftime('%Y')
		Month = strftime('%m')
		Day = strftime('%d')

		html = urlopen("http://stu.gbe.kr/sts_sci_md01_001.do?schulCode=R100000733&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=%s&schYmd=%s.%s.%s" %(meal, Year, Month, Day))
		inform = BeautifulSoup(html, "html.parser")
		meal_tb = inform.find("table", class_="tbl_type3")
		meal_thead = meal_tb.find_all("thead")
		tr = meal_tb.tbody.find_all("tr")
		food = tr[1].find_all("td", class_="textC")

		#Monday
		food_mon = food[1]
		food_mon = str(food_mon)
		food_mon = food_mon.replace('<br/>','\n')
		food_mon = food_mon.replace('</td>','')
		food_mon = food_mon.replace('<td class="textC">','\n')

		#Tuesday
		food_tue = food[2]
		food_tue = str(food_tue)
		food_tue = food_tue.replace('<br/>','\n')
		food_tue = food_tue.replace('</td>','')
		food_tue = food_tue.replace('<td class="textC">','\n')

		#Wednesday
		food_wed = food[3]
		food_wed = str(food_wed)
		food_wed = food_wed.replace('<br/>','\n')
		food_wed = food_wed.replace('</td>','')
		food_wed = food_wed.replace('<td class="textC">','\n')

		#Thursday
		food_thu = food[4]
		food_thu = str(food_thu)
		food_thu = food_thu.replace('<br/>','\n')
		food_thu = food_thu.replace('</td>','')
		food_thu = food_thu.replace('<td class="textC">','\n')

		#Friday
		food_fri = food[5]
		food_fri = str(food_fri)
		food_fri = food_fri.replace('<br/>','\n')
		food_fri = food_fri.replace('</td>','')
		food_fri = food_fri.replace('<td class="textC">','\n')

		#Saturday
		food_sat = food[6]
		food_sat = str(food_sat)
		food_sat = food_sat.replace('<br/>','\n')
		food_sat = food_sat.replace('</td>','')
		food_sat = food_sat.replace('<td class="textC">','\n')
		food_sat = food_sat.replace('<td class="textC last">','\n')

		print("요일을 선택해주세요")
		day = str(input())

		if day == "월":
			print("월요일")
			print(food_mon)
		elif day == "화":
			print("화요일")
			print(food_tue)
		elif day == "수":
			print("수요일") 
			print(food_wed)
		elif day == "목":
			print("목요일") 
			print(food_thu)
		elif day == "금":
			print("금요일") 
			print(food_fri)
		elif day == "토":
			print("토요일")
			print(food_sat)
		else:
			print("Error!")
			schoolfood()
	else:
		print("Error!")


# 현재 운영중인 서비스이기 때문에 중요한 정보는 공개하지 않습니다.

def report():
	print("----------------------------------------------------------\n"
		  "                경일 신문고 입니다.                   \n"
		  "  학교에 건의할 의견이나 학교폭력 신고를 받고 있습니다.  \n"
		  "----------------------------------------------------------\n")

	print("[1] 경일 신문고 보내기")
	print("[2] 돌아가기")
	report = int(input())

	if report == 1:
		print(	"*주의*\n"
				"부적절한 내용 전송은 처벌 대상입니다.\n"
				"사이버수사대의 로그 기록 요청에 묵인하지 않습니다.\n")
		smtp = smtplib.SMTP('smtp.gmail.com', 587)
		smtp.ehlo()
		smtp.starttls()
		smtp.login() # Gmail ID and Password

		print("서버에 로그인하였습니다. \n"
			  "제목을 입력하세요.")
		subject = str(input())

		print("내용을 입력하세요.")
		contents = str(input())

		print("위 내용으로 전송하시겠습니까? (예/아니요)\n")
		yesorno = str(input())

		if yesorno == "예":
			print("\n")
			msg = EmailMessage()
			
			msg['Subject'] = subject
			msg.set_content(contents)

			msg['From'] = ''# 발신 메일
			msg['To'] = '' #수신 메일 

			smtp.send_message(msg)

			print("성공적으로 보냈습니다!")
			main()

		else:
			print("취소합니다.")
			main()
	else:
		main()

def notice():
	print("다음 업데이트 예정일 : 2019.03.31")
	print("많은 이용 부탁드립니다.")

if __name__ == "__main__":
	main()