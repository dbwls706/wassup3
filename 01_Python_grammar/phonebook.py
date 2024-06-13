prompt = """
1. 연락처 추가
2. 연락처 전체보기
3. 검색
4. 수정
5. 삭제
6. 종료
Enter number : """
print(prompt)
num = 0
phone_list={}

while num != 6 :
    num = int(input())
    if num ==1:
        print('추가할 이름을 작성해주십시오.')
        name = input('이름: ')
        print('추가할 전화번호를 작성해주십시오.')
        phone = input('전화번호: ')
        phone_list[name] = phone
        print('전화번호가 추가되었습니다.')
    elif num ==2:
        print(phone_list)
    elif num ==3:
        print('검색할 이름을 작성해주십시오.')
        name = input('이름: ')
        print(name,' : ',phone_list[name])
    elif num == 4:
        print('수정할 이름을 작성해주십시오.')
        name = input('이름: ')
        print(phone_list[name])
        print('수정할 전화번호를 작성해주십시오.')
        phone = input('전화번호: ')
        phone_list[name]=phone
    elif num == 5:
        print('삭제할 이름을 작성해주십시오.')
        name = input('이름: ')
        del phone_list[name]
        print(name,'전화번호가 삭제되었습니다')