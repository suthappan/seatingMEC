from fpdf import FPDF
import sys

def print_seating(input_file = "final-002.csv", report_heading="",strHeading=""):


    ROW_FONT_SIZE = 16
    ROW_HEIGHT = 5.5


    COL_SEAT = 14
    COL_PAPER	=30
    COL_REGNO	=45
    COL_NAME	=65
    COL_BLANK	= 30


    
    class PDF(FPDF):
        def header(self):
            self.image('MEC_logo.png', 5,5,20)
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

        def footer(self):


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
    # Instantiation of inherited class
    pdf = PDF()
    pdf.alias_nb_pages()
    #pdf.add_page()
    pdf.set_font('Times', 'B', 14)
    page_width = 152
    current_room = ""
    row = 1
    with open(input_file) as file1:
        for line in file1:
            if row == 1:
                row = 2
                #do nothing
            else:

                firstRow = False
                #-------------------
                fields = line.count(',')
                col_width = (page_width/4)

                i=0
                for col in line.split(','):
                    cellValue=col.replace('"','')

                    if cellValue != current_room and i == 0:	#Room
                        pdf.add_page()
                        pdf.set_font('Times', 'B', 20)
                        pdf.cell(0,6,"Room No: " + cellValue + "         " + report_heading,0,1,'R')
                        pdf.set_font('Times', 'B', ROW_FONT_SIZE-1)
                        pdf.cell(COL_SEAT,ROW_HEIGHT-1,"Seat",1,0,'L')
                        pdf.cell(COL_PAPER,ROW_HEIGHT-1,"Paper",1,0,'L')
                        pdf.cell(COL_REGNO,ROW_HEIGHT-1,"RegNo",1,0,'L')
                        pdf.cell(COL_NAME,ROW_HEIGHT-1,"Name",1,0,'L')
                        pdf.cell(COL_BLANK,ROW_HEIGHT-1,"",1,1,'L')


                    elif i ==1:							#seat
                        pdf.set_font('Times', '', ROW_FONT_SIZE)
                        pdf.cell(COL_SEAT,ROW_HEIGHT,cellValue,1,0,'L')
                    elif i ==7:							#RegNo
                        pdf.set_font('Times', '', ROW_FONT_SIZE)
                        pdf.cell(COL_REGNO,ROW_HEIGHT,cellValue,1,0,'L')

                    elif i ==8:							# Name
                        pdf.set_font('Times', '', ROW_FONT_SIZE)
                        pdf.cell(COL_NAME,ROW_HEIGHT,cellValue,1,0,'L')
                        pdf.cell(COL_BLANK,ROW_HEIGHT,"",1,1,'L')


                    elif i ==5:							#Paper
                        pdf.set_font('Times', '', ROW_FONT_SIZE)
                        pdf.cell(COL_PAPER,ROW_HEIGHT,cellValue,1,0,'L')

                    if i == 0:
                        current_room = cellValue


                    i = i + 1
                #-------------------



    pdf.output('tmp/seating.pdf', 'F')


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
