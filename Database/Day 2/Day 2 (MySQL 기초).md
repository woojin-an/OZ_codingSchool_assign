### SQL의 주요 언어 유형
1. DDL (Data Definition Language) : 데이터베이스의 구조를 정의하는데 사용되는 언어 유형
    * CREATE : 새로운 테이블이나 데이터베이스 생성
    * ALTER : 기존 테이블이나 데이터베이스 구조 수정
    * DROP : 테이블이나 데이터베이스 삭제

2. DML (Data Manipulation Language): 데이터베이스 내의 데이터를 처리하는데 사용되는 언어입니다.
    * SELECT : 데이터베이스에서 데이터 조회
    * INSERT : 테이블에 새로운 데이터 추가
    * UPDATE : 테이블의 기존 데이터 수정
    * DELETE : 테이블에서 데이터 삭제

3. DCL (Data Control Language): 데이터베이스 사용자의 권한을 관리하고 데이터 접근을 제어하는데 사용되는 언어입니다.
    * GRANT : 사용자에게 특정 데이터에 대한 접근 권한 부여
    * REVOKE : 사용자의 특정 데이터 접근 권한 제거

4. TCL (Transaction Control Language): 데이터베이스 내의 트랜잭션을 관리하는데 사용되는 언어 입니다.
    * COMMIT : 트랜잭션을 완료하고, 데이터베이스 변경사항을 영구적으로 저장
    * ROLLBACK : 트랜잭션을 취소하고, 마지막 COMMIT 이후의 모든 변경사항을 되돌림
    * SAVEPOINT : 트랜잭션 내 특정 지점을 마킹하여 필요시 그 지점으로 되돌릴 수 있음

각각의 언어 유형은 데이터베이스의 다양한 측면을 다루며, 데이터베이스의 구조를 정의하고(DDL), 데이터를 처리하며(DML), 사용자 권한을 관리하고(DCL), 트랜잭션을 제어하는(TCL) 역할을 함. 이러한 분류를 통해 데이터베이스 시스템의 효과적인 관리와 운영이 가능함