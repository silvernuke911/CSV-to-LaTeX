import pandas as pd
import numpy as np

################  INSTRUCTIONS  #################

# Put this python script and the csv file of choice on the same directory folder

# At the bottom is initialization code. Go to the bottom of the code after reading this line. Basically, the finename of the csv, and others.
#   Filename        := name of the csv file
#   Table Create    := Create a table format or just format the content to a latex compilable expresssion. Advisable, and default, is true
#   Math Format     := Formats the titles to '$$' for latex math environment. Default is true
#   Captions        := Your table caption
#   Label           := Your table label for referencing on other parts of the document

# Place the required shit and run the code. It outputs a txt file with the latex compatible code and data with it
# Go fuck yourself

# Code by : SilverNuke911

##################################################

def column_extractions(cols, df):
    # Extract columns based on indices and return as list of lists
    return [df.iloc[:, i].tolist() for i in cols]

def row_extractions(indiv_columnlist):
    # Zip columns into rows
    return list(zip(*indiv_columnlist))

def latex_compatability_row(rowlist,math=False):
    rowtext=''
    if math==False:
        for i in range(len(rowlist)):
            if i==0:
                rowtext+=(str(rowlist[i])+'\t')
            else:
                rowtext+=('& '+str(rowlist[i])+'\t')
        rowtext+=r'\\'
    if math==True:
        for i in range(len(rowlist)):
            if i==0:
                rowtext+=('$'+str(rowlist[i])+'$'+'\t')
            else:
                rowtext+=('& '+'$'+str(rowlist[i])+'$'+'\t')
        rowtext+=r'\\'
    return rowtext

def row_text_creation(indiv_rowlist):
    # Convert each row to LaTeX-compatible string
    return [latex_compatability_row(row) for row in indiv_rowlist]

def write_to_txt(linelist):
    # Write LaTeX-compatible rows to text file
    with open(f'{filename}_latex_compatible.txt', 'w') as file:
        for line in linelist:
            file.write(line + '\n')
            print(f'Writing to file: {line}')  # Print each line as it's written

def write_alignment(columns, char='c'):
    # Create alignment string for LaTeX table
    return ' '.join([char] * columns)
def write_table(column_name_list, linelist, textlist):
    # Write complete LaTeX table structure to text file
    command_list = textlist[0] + [
        '\t' * 2 + f'{latex_compatability_row(column_name_list, math=True)}' + '\n'
    ] + textlist[1] + [
        '\t' * 2 + f'{line}' + '\n' for line in linelist
    ] + textlist[2]

    with open(f'{filename}_latex_compatible.txt', 'w') as file:
        for line in command_list:
            file.write(line)
            print(line.replace('\n', ''))

def text_lists(captions, labels, alignment_text):
    # Create LaTeX commands for table structure
    return [
        [
            r'\begin{table}[h!]' + '\n',
            '\t' + r'\centering' + '\n',
            '\t' + r'\caption{' + f'{captions}' + '}' + '\n',
            '\t' + r'\begin{tabular}{' + f'{alignment_text}' + '}' + '\n',
            '\t' + r'\toprule' + '\n'
        ],
        ['\t' + r'\midrule' + '\n'],
        [
            '\t' + r'\bottomrule' + '\n',
            '\t' + r'\end{tabular}' + '\n',
            '\t' + r'\label{' + f'{labels}' + '}' + '\n',
            r'\end{table}'
        ]
    ]

def main():
    #   column creation
    data=pd.read_csv(filename)
    column_name_list=pd.read_csv(filename, nrows=1).columns.tolist()
    df = pd.DataFrame(data)
    cols = list(range(len(column_name_list)))
    m = len(cols)

    #   column extraction
    indiv_columnlist = column_extractions(cols,df)

    #   row extraction
    indiv_rowlist = row_extractions(indiv_columnlist)

    #   row text extraction
    linelist = row_text_creation(indiv_rowlist)
    alignment_text = write_alignment(m)
    textlist = text_lists(captions,labels,alignment_text)

    #   writing to file
    print('Currently encoding text'+'\n')
    if table_create==True:
        write_table(column_name_list,linelist,textlist)
    else:
        write_to_txt(linelist)
    print('\n'+f'File {filename} successful encoded!')

#   Initialization
filename        = 'plotto.csv'
table_create    = True
math_format     = True
captions        = 'Telescope Assembly Results'
labels          = 'tab: TelAssem'

if __name__=='__main__':
    main()
