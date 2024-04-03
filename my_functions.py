from fpdf import FPDF
import sys
import csv

ROW_FONT_SIZE = 16
ROW_HEIGHT = 5.5



# Define a function to sort the CSV file based on multiple columns
def sort_csv(input_file, output_file, sort_columns):
    # Read the CSV file
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        data = list(reader)
        header = data[0]  # Extract header row
        data = data[1:]   # Remove header row from the data


    # Sort the data based on specified columns
    sorted_data = sorted(data, key=lambda x: (x[6], x[4]))

    # Write the sorted data to a new CSV file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(sorted_data)





def print_seating(input_file="final-002.csv", report_heading="", strHeading=""):
	COL_SEAT = 14
	COL_PAPER	=30
	COL_REGNO	=45
	COL_NAME	=65
	COL_BLANK	= 30
	column_width = COL_BLANK
	column_height = ROW_HEIGHT

	INDEX_ROOM = 2
	INDEX_SEAT = 3
	INDEX_NAME = 4
	INDEX_REGNO = 5
	#INDEX_SLOT = 6
	INDEX_PAPER = 7

	class PDF(FPDF):
		def header(self):
			#header start
			self.image('MEC_logo.png', 5,5,20)
			# Arial bold 15
			self.set_text_color(128,128,128)
			self.set_font('Arial', 'B', 15)
			# Move to the right
			self.cell(80)
			# Title
			self.cell(1, 5, 'Model Engg. College, Thrikkakara', 0, 1, 'C')
			self.set_font('Arial', 'B', 15)
			self.cell(80)
			self.set_text_color(0,0,0)
			self.cell(1, 5, 'Examination Seating Arrangement' + "-" + strHeading, 0, 1, 'C')
			# Line break
			#self.ln(20)
			self.ln(2)
			#header end
			
		def footer(self):
		
			#footer start
			self.set_y(-28)
			pdf.set_font('Times', 'B', 14)			
			pdf.cell(0,17,"Absentees:                                                               Invigilator : ________________",0,1,'L')  
			#pdf.cell(0,17,"Absentees : ",1,1,'L')  
			start_reporting = True		

			# Position at 1.5 cm from bottom
			self.set_y(-10)
			# Arial italic 8
			self.set_font('Arial', 'I', 8)
			# Page number
			self.cell(0, 7, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
			# footer end
			
			
			
	# Instantiation of inherited class
	pdf = PDF()
	pdf.alias_nb_pages()
	#pdf.add_page()
	pdf.set_font('Times', 'B', 14)
	#for i in range(1, 41):
	#   pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
	page_width = 152
	#printRoom=True
	current_room = ""
	row = 1
	print_row = 0
	with open(input_file) as file1:
		#file open start
		print_row=0
		for line in file1:
			if row == 1:
				row = 2
				#do nothing
			else:
			
				#------------------- Else START
				fields = line.count(',')

				i=1
				for col in line.split(','):
					cellValue=col.replace('"','')
					#input("Start i="+str(i) + ", cellValue=" + cellValue)
					
					if (cellValue != current_room and i == INDEX_ROOM) or (print_row == 45 and i == INDEX_ROOM):	#Room column
						pdf.add_page()
						pdf.set_font('Times', 'B', 20)					
						pdf.cell(0,6,"Room No: " + cellValue + "         " + report_heading,0,1,'R')
						pdf.set_font('Times', 'B', ROW_FONT_SIZE-1)					
						pdf.cell(COL_SEAT,ROW_HEIGHT-1,"Seat",1,0,'L')	
						pdf.cell(COL_NAME,ROW_HEIGHT-1,"Name",1,0,'L')		
						pdf.cell(COL_REGNO,ROW_HEIGHT-1,"RegNo",1,0,'L')	
						pdf.cell(COL_PAPER,ROW_HEIGHT-1,"Paper",1,0,'L')	
						pdf.cell(COL_BLANK,ROW_HEIGHT-1,"",1,1,'L')			
						print_row = 1
						
					elif i ==INDEX_SEAT:							#seat	 column
						#pdf.set_font('Times', '', ROW_FONT_SIZE)
						#pdf.cell(COL_SEAT,ROW_HEIGHT,cellValue,1,0,'L')
						#input(" i="+str(i) + ", cellValue=" + cellValue)
						font_name = 'Times'; font_size = ROW_FONT_SIZE; column_width = COL_SEAT; column_height = ROW_HEIGHT;font_style="R"
						
					elif i == INDEX_PAPER:							#Paper column
						#pdf.set_font('Times', '', ROW_FONT_SIZE)
						#pdf.cell(COL_PAPER,ROW_HEIGHT,cellValue,1,0,'L')
						#input(" i="+str(i) + ", cellValue=" + cellValue)
						font_name = 'Times';font_size = ROW_FONT_SIZE;column_width = COL_PAPER;column_height = ROW_HEIGHT;font_style="R"

						
					elif i ==INDEX_REGNO:							#RegNo column
						#pdf.set_font('Times', '', ROW_FONT_SIZE)
						#pdf.cell(COL_REGNO,ROW_HEIGHT,cellValue,1,0,'L')
						#input(" i="+str(i) + ", cellValue=" + cellValue)
						font_name = 'Times';font_size = ROW_FONT_SIZE;column_width = COL_REGNO; column_height = ROW_HEIGHT;font_style="R"
						
					elif i ==INDEX_NAME:							# Name column
						#pdf.set_font('Times', '', ROW_FONT_SIZE)
						#pdf.cell(COL_NAME,ROW_HEIGHT,cellValue,1,0,'L')			
						font_name = 'Times';font_size = ROW_FONT_SIZE;column_width = COL_NAME; column_height = ROW_HEIGHT;font_style="R"


					if i in (3,4,5,7):
						pdf.set_font(font_name, '', font_size)
						pdf.cell(column_width,column_height,cellValue,1,0,'L')
						#input(cellValue)
					if i == 7:
						pdf.cell(COL_BLANK,ROW_HEIGHT,"",1,1,'L')	

					#input(" i="+str(i) + ", cellValue=" + cellValue)
						
						

					
					#input("Start i="+str(i) + ", cellValue=" + cellValue + ", current_room = " + current_room)	
					if i == INDEX_ROOM:
						current_room = cellValue	
						#input("Room Change,  i="+str(i) + ", cellValue=" + cellValue + ", current_room = " + current_room)		
						
					i = i + 1
				#------------------- Else END
			#file open end	
			print_row += 1

		pdf.output('tmp/seating.pdf', 'F')
#-------------------------------------------------------------------------------------------------------------------------------------------------- -
#-------------------------------------------------------------------------------------------------------------------------------------------------- -

def summarise(raw_file):
    # generate summary csv from "final-002.csv"

    room_data = {}
    subj_data = {}
    room_total = {}
    total = 0
    in_file = open(raw_file, 'r')

    for line in in_file:
        line = line.strip()
        if line.startswith("No"):
            continue
        line = line.replace(" ", "")
        line = line.replace(",,", ",")  # Sanitization
        data = line.split(",")
        _, room, sn, name, rn, slot, subj = data
        room = room.strip()
        subj = subj.strip()
        room_data.setdefault(room, {}).setdefault(subj, 0)
        room_data[room][subj] += 1
        subj_data.setdefault(subj, 0)
        subj_data[subj] += 1
        room_total.setdefault(room, 0)
        room_total[room] += 1
        total += 1

    sep = '","'
    subj_list = sorted(subj_data.keys())
    title = '"Room' + sep + sep.join(subj_list) + sep + 'Total"'

    # Here is where our output goes.
    out_file = open("tmp/summary.csv", "w")

    print(title, file=out_file)

    for room_name in sorted(room_data.keys()):
        det = [room_name]
        for subj_name in subj_list:
            det.append(str(room_data.get(room_name, {}).get(subj_name, 0)))
        det.append(str(room_total.get(room_name, 0)))
        det_str = '"' + sep.join(det) + '"'
        print(det_str, file=out_file)

    sum_list = ['Total']
    for subj_name in sorted(subj_data.keys()):
        sum_list.append(str(subj_data[subj_name]))
    sum_list.append(str(total))
    sum_str = '"' + sep.join(sum_list) + '"'
    print(sum_str, file=out_file)

    # Close files
    if in_file is not sys.stdin:
        in_file.close()

    out_file.close()
    
#= ================= =
   
    
def print_summary(report_heading,strHeading):
	input_file = "./tmp/summary.csv"
	class PDF(FPDF):
		def header(self):
			# Logo
			#self.image('MEC_logo.png', 5, 5, 33)
			self.image('./MEC_logo.png', 5,5,20)
			
			# Arial bold 15
			self.set_text_color(128,128,128)
			self.set_font('Arial', 'B', 15)
			# Move to the right
			self.cell(80)
			# Title
			self.cell(1, 5, 'Model Engg. College, Thrikkakara', 0, 1, 'C')
			self.set_font('Arial', 'B', 15)
			self.cell(80)
			self.set_text_color(0,0,0)
			self.cell(1, 5, 'Examination Seating Arrangement' + "-" + strHeading , 0, 1, 'C')
			self.set_font('Arial', 'B', 20)
			self.cell(0, 7, "", 0, 1, 'R')
			self.cell(0, 4, report_heading, 0, 1, 'R')
			
			
			
			
			# Line break
			self.ln(20)

		def footer(self):
			# Position at 1.5 cm from bottom
			self.set_y(-15)
			# Arial italic 8
			self.set_font('Arial', 'I', 8)
			# Page number
			self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
			
	# Instantiation of inherited class
	pdf = PDF()
	pdf.alias_nb_pages()
	pdf.add_page()
	pdf.set_font('Times', 'B', 14)
	#for i in range(1, 41):
	#   pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
	page_width = 152
	with open('./tmp/summary.csv') as file1:    	 
		for line in file1:
			pdf.set_font('Times', 'B', 14)
			fields = line.count(',')

						
			col_width = (page_width/(fields))*1	#.18		# use this when subject codes are of reasonable length
			#col_width = (page_width/(fields))*1.15	#.18		# use this when subject codes are of reasonable length
			#col_width = (page_width/(fields+1))		# use this when subject codes are of reasonable length
			#col_width = (page_width/(fields*0.85))	# when the Subject codes are very big and flow over

			i=0
			for col in line.split(','):
				cellValue=col.replace('"','')
				if cellValue=="0":
					cellValue=""
					
				if i== fields:
					nextLine=1
				else:
					nextLine=0
				if i== 0:
					pdf.set_font('Times', 'B', 13)
				else:
					pdf.set_font('Times', '', 14)	
					
				pdf.cell(col_width,10,cellValue,1,nextLine,'C')
				i = i + 1
			pdf.set_font('Times', '', 14)
	pdf.set_font('Times', 'B', 16)			
	pdf.cell(0,10,"Total number of students : " + cellValue,0,nextLine,'R')  
	

	
	
	
	
	pdf.output('tmp/summary.pdf', 'F')
