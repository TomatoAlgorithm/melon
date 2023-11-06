def solution(today, terms, privacies):
    answer = []
    
    for i, privacy in enumerate(privacies,0) :
        for term in terms:
            if(privacy[-1] == term[0]):
                todayarr = today.split('.')
                privacyday = privacy.split(' ')[0].split('.')
                month = int(privacyday[1]) + int(term[-2:])
                day = int(privacyday[2]) - 1
                year = int(privacyday[0])
                
                

                if(day == 0):
                    month -= 1
                    day=28
                if(month == 0):
                    year -= 1
                    month = 12
                if(month > 12):
                    year += month//12
                    month = month % 12
                    if(month == 0):
                        year -= 1
                        month = 12
                
                print(f'year = {year} / month ={month} / day = {day}')


                if(int(todayarr[0]) < year):
                    answer.append(i)
                    break
                elif(int(todayarr[0]) == year):
                    if(int(todayarr[1]) < month):
                        answer.append(i)
                        break
                    elif(int(todayarr[1]) == month):
                        if(int(todayarr[2]) > day):
                            answer.append(i)
                            break
                break
           
    return answer

print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))