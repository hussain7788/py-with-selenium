import time
import logging
from fpdf import FPDF
import os

# Ubuntu
# file_name = str(int(time.time()))
dst = 'test1'

feeder_dict = {
'state':"andhra pradesh",
'brokers_representative':"somename",
'first_name':"Hussain",
'middle_name':"",
'last_name':"valli",
'suffix_name':"Gng",
'alter_first_name':"Mahammad",
'alter_middle_name':"",
'alter_last_name':"ali",
'alter_suffix_name':"Alamuri",
'date_from_feeder':"23/05/2022",
'loan_number':"123456789",
'date':"DATE"

}
def formatter(*args) : 
    return ' '.join([arg for arg in args if arg])

def format_date(date_value) : 
    return date_value.split('T')[0]


def generate_pdf_for_dc(feeder=dict()):
    pdf = FPDF('P', 'mm', 'Letter')
    logging.info("Function started for generating PDF file for state DC")
    # try:
    logging.info("FPDF started making upo the template...")
    #: Add page
    pdf.add_page()

    # Custom Variables
    state = feeder.get('state')
    brokers_representative = feeder.get('brokers_representative')
    first_name = feeder.get('first_name')
    middle_name = feeder.get('middle_name')
    last_name = feeder.get('last_name')
    suffix_name = feeder.get('suffix_name')
    alter_first_name = feeder.get('alter_first_name')
    alter_middle_name = feeder.get('alter_middle_name')
    alter_last_name = feeder.get('alter_last_name')
    alter_suffix_name = feeder.get('alter_suffix_name')
    date_from_feeder = feeder.get('date')

    borrower1 = formatter(first_name , middle_name , last_name , suffix_name)
    borrower2 = formatter(alter_first_name , alter_last_name ,\
        alter_middle_name , alter_suffix_name)
    date_from_feeder = format_date(date_from_feeder) # Only need the date value

    pdf.set_font('times', 'B', 10)
    pdf.cell(180, 30, "DISTRICT OF COLUMBIA", ln=True, align='R')
    pdf.set_font('times', 'B', 16)
    pdf.cell(0, 20, "DISCLOSURE OF DUAL CAPACITY", ln=True, align='C')

    pdf.set_font('times', 'B', 8)
    pdf.cell(0, 0, "Pursuant to D.C. Code Ann. § 26-1114(b)(3)(A).", ln=True, align='C')

    pdf.set_font('times', '', 10)
    pdf.cell(120, 50, f"Brokers Representative: {brokers_representative}", align='C')
    pdf.cell(80, 50, f"Borrower: {borrower1}", ln=True)
    pdf.cell(120, -20, "Title: Mortgage Loan Officer", align='C')
    pdf.cell(80, -20, f"Borrower: {borrower2}", ln=True)
    pdf.cell(120, 50, f"Date: {date_from_feeder}", align='C')
    pdf.cell(80, 50, f"Date: {date_from_feeder}", ln=True)

    para = "WE HAVE OFFERED TO ASSIST YOU IN OBTAINING A MORTGAGE LOAN. IF WE ARE SUCCESSFUL IN OBTAINING A LOAN FOR YOU, WE WILL CHARGE AND COLLECT FROM YOU A FEE NOT TO EXCEED 1 % OF THE LOAN AMOUNT. THIS FEE IS IN ADDITION TO ANY OTHER FEE WE MAY RECEIVE IN CONNECTION WITH THE SALE OR PURCHASE OF THE REAL ESTATE THAT WILL SECURE THE LOAN. WE DO NOT REPRESENT ALL OF THE LENDERS IN THE MARKET AND THE LENDERS WE DO REPRESENT MAY NOT OFFER THE LOWEST INTEREST RATES OR BEST TERMS AVAILABLE TO YOU. YOU ARE FREE TO SEEK A LOAN WITHOUT OUR ASSISTANCE, IN WHICH EVENT YOU WILL NOT BE REQUIRED TO PAY US A FEE FOR THAT SERVICE. THE BORROWER ACKNOWLEDGES HAVING READ AND UNDERSTOOD THIS DISCLOSURE OF DUAL CAPACITY AND HAVING RECEIVED A COPY HEREOF"
    pdf.multi_cell(0, 6, para, align='C')

    paraTwo = "This disclosure must be provided at the time brokerage services are offered when a mortgage broker, or any person affiliated with such mortgage broker, has otherwise acted as a real estate broker, agent, or salesperson in connection with the sale of real estate which secures the mortgage loan and such mortgage broker or affiliated person has received or will receive any other compensation or thing of value from the lender, borrower, seller, or any other person."
    pdf.cell(0, 10, '', ln=True)
    pdf.set_font('times', '', 9)
    pdf.multi_cell(0, 5, paraTwo, border=True)

    logging.info("Processing PDF generation....")
    pdf.output('{}.pdf'.format(dst))
    logging.info(
        "Walaahhhh! PDF file generated successfully for state DC and saved")

    # Returing the output path where the pdf is stored
    return f'{dst}.pdf'
    # except Exception as e:
    #     logging.info("Error Occured : {}".format(e))
    #     logging.info("#pdfcheck : Something went wrong while generating pdf")
    #     return False

# data = generate_pdf_for_dc(feeder_dict)
# print(data)

dst = 'test2'
def generate_pdf_for_ms(feeder=dict()):
    pdf = FPDF('P', 'mm', 'Letter')
    logging.info("Function started for generating PDF file for state MS")
    try:
        logging.info("FPDF started making upo the template...")

        # Custom variables
        loan_number = feeder.get('loan_number', " ")

        #: Add page
        pdf.add_page()
        pdf.set_font('times', 'B', 10)
        pdf.set_font('times', 'BU', 13)
        pdf.cell(0, 10, '', ln=True)
        pdf.cell(0, 20, "MISSISSIPPI MORTGAGE ORIGINATION AGREEMENT",
                 ln=True, align='C')

        pdf.set_font('times', '', 9)
        pdf.cell(140, 10, '')
        pdf.cell(0, 5, f"Loan#: {loan_number}", ln=True)

        pdf.cell(140, 2, '')
        pdf.cell(0, 20, "MIN: N/A",
                 ln=True)

        paraOne = "As required by Mississippi Law, Animo Mortgage Company, LLC d/b/a GloriFi Mortgage , has secured a bond issued by The Cincinnati Insurance Company,NAIC #10677 a surety company authorized to do business in this state. A certified copy of this bond is filed with the Mississippi Commissioner of Banking and Consumer Finance."

        paraOne = "As required by Mississippi Law, Animo Mortgage Company, LLC d/b/a GloriFi Mortgage , has secured a bond issued by The Cincinnati Insurance Company, NAIC #10677 a surety company authorized to do business in this state. A certified copy of this bond is filed with the Mississippi Commissioner of Banking and Consumer Finance."
        pdf.set_font('times', '', 10)
        pdf.multi_cell(0, 5, paraOne)

        pdf.cell(0, 5, '', ln=True)
        pdf.cell(
            0, 10, 'As a borrower you are protected under the Mississippi S.A.F.E. Mortgage Act.', ln=True)

        pdf.cell(0, 2, '', ln=True)
        pdf.cell(0, 10, 'Complaints against a licensee may be made by contacting the:',
                 ln=True)

        pdf.cell(15, 2, '')
        pdf.cell(0, 5, 'Mississippi Department of Banking and Consumer Finance',
                 ln=True)

        pdf.cell(15, 2, '')
        pdf.cell(0, 5, 'P.O. Drawer 12129', ln=True)

        pdf.cell(15, 2, '')
        pdf.cell(0, 5, 'Jackson, MS 39236-2129', ln=True)

        pdf.cell(0, 10, '', ln=True)
        pdf.cell(0, 5, 'I hereby acknowledge that I have read and understand this agreement.',
                 ln=True)

        pdf.cell(0, 10, '', ln=True)
        pdf.cell(0, 5, '_______________________________________________',
                 ln=True)

        logging.info("Processing PDF generation....")
        pdf.output('{}.pdf'.format(dst))
        logging.info(
            "Walaahhhh! PDF file generated successfully for state MS and saved")
        # Returing the output path where the pdf is stored
        return f'{dst}.pdf'
    except Exception as e:
        logging.info("Error Occured : {}".format(e))
        logging.info("#pdfcheck : Something went wrong while generating pdf")
        return False

data2 = generate_pdf_for_ms(feeder_dict)
print(data2)

