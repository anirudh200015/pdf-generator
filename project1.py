from fpdf import FPDF
title="python pdf generator"
class pdf_file(FPDF):
    def header(self):
        self.set_font('arial','B',17)
        w=self.get_string_width(title)+6
        self.set_x((210-w)/2)
        self.set_text_color(220,50,50)
        self.cell(w,10,title,1,1,'C',1)
    def footer(self):
        self.set_font('arial','I',10)
        self.set_y(-15)
        self.set_text_color(0,220,55)
        self.cell(0,10,'Page'+str(self.page_no()),0,0,'C')
    def chapter_title(self,num,label):
        self.set_font('Arial','',12)
        self.set_fill_color(200,220,255)
        self.cell(0,6,'Chapter %d : %s' %(num,label),0,1,'L',1)
        self.ln(4)
    def chapter_body(self,name):
        with open(name,'rb') as th:
            txt=th.read().decode('latin-1')
        self.set_font('Times','',12)
        self.multi_cell(0,5,txt)
        self.ln()
        self.set_font('','I')
        self.cell(0,5,'(end)')
    def print_chapter(self,num,title,name):
        self.add_page()
        self.chapter_title(num,title)
        self.chapter_body(name)
pdf=pdf_file()
pdf.set_title(title)
pdf.print_chapter(1,'pdf converter using python','file.txt')
pdf.output('project_1.pdf','F')
    
        
