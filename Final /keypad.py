import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MATRIX = [['1','2','3','A'],
          ['4','5','6','B'],
          ['7','8','9','C'],
          ['*','0','#','D']]

ROW = [18,23,24,12]
COL = [4,17,27,22]

for j in range(4) : 
	GPIO.setup(COL[j],GPIO.OUT)
	GPIO.output(COL[j],1)

for i in range(4) : 
	GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

instr = ' '
indicator = True
reindicator = False

try:
	while(indicator):
		for j in range(4):
			GPIO.output(COL[j],0)
			for i in range(4):
				if GPIO.input(ROW[i])==0:
					if MATRIX[i][j] == 'A':
						if reindicator==False:
							continue
						print 'Enter Amount : '
						instr = ''
						time.sleep(1)
					elif MATRIX[i][j] == 'B':
						if reindicator == False:
							continue
						print 'Transaction Successful'
						print 'Amount :', instr 
						instr = ''
						indicator = False
						reindicator = False
					elif MATRIX[i][j] == 'C':
						if reindicator == False:
							continue
						print 'Transaction Cancelled'
						indicator = False
						reindicator = False
					elif MATRIX[i][j] == 'D':
						print 'Recharge Mood On'
						reindicator = True 
					elif MATRIX[i][j] == '0':
						if reindicator == False:
							continue
						instr += MATRIX[i][j]
						print instr
						time.sleep(0.5)
					elif MATRIX[i][j] == '1':
						if reindicator == False:
							continue
						instr += MATRIX[i][j]
						print instr
						time.sleep(0.5)
					elif MATRIX[i][j] == '2':
						if reindicator == False:
							continue
						instr += MATRIX[i][j]
						print instr
						time.sleep(0.5)
					elif MATRIX[i][j] == '3':
						if reindicator == False:
							continue
						instr += MATRIX[i][j]
						print instr
						time.sleep(0.5)
					elif MATRIX[i][j] == '4':
						if reindicator == False:
							continue
						instr += MATRIX[i][j]
						print instr
						time.sleep(0.5)
					elif MATRIX[i][j] == '5':
						if reindicator == False:
							continue
						instr += MATRIX[i][j]
						print instr
						time.sleep(0.5)
					elif MATRIX[i][j] == '6':
						if reindicator == False:
							continue
						instr += MATRIX[i][j]
						print instr
						time.sleep(0.5)
					elif MATRIX[i][j] == '7':
						if reindicator == False:
							continue
						instr += MATRIX[i][j]
						print instr
						time.sleep(0.5)
					elif MATRIX[i][j] == '8':
						if reindicator == False:
							continue 
						instr += MATRIX[i][j]
						print instr
						time.sleep(0.5)
					elif MATRIX[i][j] == '9':
						if reindicator == False:
							continue
						instr += MATRIX[i][j]
						print instr
						time.sleep(0.5)
					else:
						time.sleep(0.2)

					while(GPIO.input(ROW[i]) == 0):
						pass
			GPIO.output(COL[j],1)

except KeyboardInterrupt:
	GPIO.cleanup()
