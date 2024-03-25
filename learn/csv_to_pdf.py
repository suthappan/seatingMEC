from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas




def create_pdf_from_text_file(input_file, output_file):
    # Create a PDF canvas
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    # Open the text file and read each line
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Set the initial y coordinate for drawing text
    y = height - 50

    # Set the font and font size
    c.setFont("Helvetica", 12)

    # Iterate over each line and draw it on the PDF canvas
    print_line = 0
    for line in lines:
   
        # Draw the line on the canvas
        c.drawString(50, y, line.strip())
        # Move to the next line
        y -= 20

        # Check if the page is full, if so, create a new page
        if y <= 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 50

    # Save the PDF file
    c.save()

# Usage example
input_file = 's4.csv'  # Change this to your input text file
output_file = 'output.pdf'  # Change this to your desired output PDF file

create_pdf_from_text_file(input_file, output_file)

