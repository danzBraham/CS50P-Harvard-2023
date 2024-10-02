from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Set the font and font size for the header
        self.set_font("helvetica", "B", 36)
        # Move to the right to center the header
        self.cell(80)
        # Print the header text
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Move to the next line after printing the header
        self.ln(20)


def main():
    # Prompt the user for their name
    name = input("Name: ")
    # Create a new PDF object with custom header
    pdf = PDF()
    # Add a new page to the PDF
    pdf.add_page()
    # Add an image to the PDF (assuming "shirtificate.png" is in the current directory)
    pdf.image("./shirtificate.png", w=pdf.epw)
    # Set the font and font size for the main text
    pdf.set_font("helvetica", size=20)
    # Set the text color to white
    pdf.set_text_color(255, 255, 255)
    # Move to the right to center the main text
    pdf.cell(80)
    # Move up to position the main text vertically
    pdf.cell(30, -250, f"{name} took CS50", align="C")
    # Output the PDF to a file named "shirtificate.pdf"
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
