import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

MATRIX = [['1','2','3','A'],
          ['4','5','6','B'],
          ['7','8','9','C'],
          ['*','0','#','D']]

ROW = [12,16,18,32]
COL = [7,11,13,15]

for j in range(4) : 
	GPIO.setup(COL[j],GPIO.OUT)
	GPIO.output(COL[j],1)

for i in range(4) : 
	GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

instr = ' '
indicator = True

try:
	while(indicator):
		for j in range(4):
			GPIO.output(COL[j],0)
			for i in range(4):
				if GPIO.input(ROW[i])==0:
					if MATRIX[i][j] == 'A':
						instr = ''
						time.sleep(1)
					elif MATRIX[i][j] == 'B':
						print 'Transaction Successful'
						print 'Amount :', instr 
						instr = ''
					elif MATRIX[i][j] == 'C':
						print 'Transaction Cancelled'
						indicator = False
					elif MATRIX[i][j] == '0':
						instr += MATRIX[i][j]
						time.sleep(0.5)
					elif MATRIX[i][j] == '1':
						instr += MATRIX[i][j]
						time.sleep(0.5)
					elif MATRIX[i][j] == '2':
						instr += MATRIX[i][j]
						time.sleep(0.5)
					elif MATRIX[i][j] == '3':
						instr += MATRIX[i][j]
						time.sleep(0.5)
					elif MATRIX[i][j] == '4':
						instr += MATRIX[i][j]
						time.sleep(0.5)
					elif MATRIX[i][j] == '5':
						instr += MATRIX[i][j]
						time.sleep(0.5)
					elif MATRIX[i][j] == '6':
						instr += MATRIX[i][j]
						time.sleep(0.5)
					elif MATRIX[i][j] == '7':
						instr += MATRIX[i][j]
						time.sleep(0.5)
					elif MATRIX[i][j] == '8':
						instr += MATRIX[i][j]
						time.sleep(0.5)
					elif MATRIX[i][j] == '9':
						instr += MATRIX[i][j]
						time.sleep(0.5)
					else:
						time.sleep(0.2)

					while(GPIO.input(ROW[i]) == 0):
						pass
			GPIO.output(COL[j],1)

except KeyboardInterrupt:
	GPIO.cleanup()
