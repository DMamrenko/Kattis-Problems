#Saving Daylight
while True:
    try:
        #taking in day info
        month, day, year, start_time, end_time = input().split()
        starth, startm = start_time[:start_time.index(':')], start_time[start_time.index(':')+1:]
        endh, endm = end_time[:end_time.index(':')], end_time[end_time.index(':')+1:]
        start, end = int(starth)*60+int(startm), int(endh)*60+int(endm)
        ansh, ansm= (end-start)//60, (end-start)%60
        print(month, day, year, ansh, 'hours', ansm, 'minutes')
    except EOFError:
        break
