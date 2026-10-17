while True:
    ga, se, alpha = input().split()
    # 이렇게만 적으면 종료 조건이 없어서 에러 뜸
    ga ,se = int(ga), int(se)
    print(ga*se)
    if alpha =="C":
        break