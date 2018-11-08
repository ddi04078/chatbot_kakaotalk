# chatbot_kakaotalk

학부 연구로 카카오톡 챗봇을 만든다. 

[기획서]

1. 차례
  - 개발 진행 상황 
  - 학과 챗봇에서 제공할 서비스
  - 다른 챗봇 서비스 분석 

2. 개발 진행 상황 : 환경세팅
  (1) Django 설치, 프로젝트 생성 및 환경설정, 코드작성
  (2) nodejs 설치, js 파일 생성 및 각종 모듈 설치, 코드 작성, 포트 개방
  (3) php 이용 : 사용자가 선택한 버튼 입력값에 대해 json으로 답변
      => 카카오톡 API 테스트에서 keyboard FAIL 415 에러 
      => 코드와 프로그램 문제가 아닌듯 하다 !

      서버를 구축하고 고정 IP를 할당받은 후,IP를 공유하며 챗봇 구축을 위한 환경설정을 하기로 결정
  (4)
      AWS(아마존 서버) 가입, EC2 설정
      탄력적 IP 할당 받음 
      보안 그룹 설정
      포트 오픈 (http, ssh)
      ssh 접속 설정
      ssh연결을 통해 IP로 서버 공유


3. 학과 챗봇에서 제공할 서비스
  (1) 카테고리 : 인턴 / 장학금 / 교수진 / 조교(컴프, 헬퍼, 랩애니웨어) / 공모전 / 장소 대여(강의실대여, 철야신청) 
              / 안전교육 / 취업공고문 / 졸업 기준 / 학번별 이수체계도 / UROP / (랜덤 정보 : 기타 학과 홈페이지에 있는 다른 유용한 정보) 
              / 학과 사무실 전화번호 / 학과 홈페이지 
      => 버튼 식으로 입력을 받은 뒤, 맞는 url 또는 정보를 제공
      
  (2) 1:1채팅 : 기존의 ‘국민대CS’ 
      => 직접 답변해주는 방식
  
  (3) 건의사항 
      => 익명 오픈채팅방이나 구글폼으로 연결해 건의사항을 모음


4. 다른 챗봇 서비스 분석
  (1) 아시아나 항공 챗봇
    - 버튼 형식과 대화 형식이 공존
    - 총 16개의 다양한 질문으로 구성
    - 영어와 한국어를 지원
    - 간단한 질문 같은 경우는 대화 가능
    - 일부 문의 내용은 항공사 홈페이지로 바로 연결하여 확인할 수 있도록 서비스가 되어있음
    - 예약확인 경우 예약 번호를 입력하면 확인 가능하여 편리하게 이용가능
    
  (2) 현대카드 Buddy 챗봇
    - 버튼 형식 X
    - 완벽하진 않지만, 질문의 일부만 입력해도 분석해서 답해줌.
