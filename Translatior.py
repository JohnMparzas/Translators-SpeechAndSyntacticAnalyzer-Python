# giannis mparzas 2765 cse42765
#stous suntaktikous kanones opou - antikatesthsa me _ 
import string
count=0
ist=""

def lektikos():
  global count,ist
  lektikh=""
  while count<len(ist):
    if count==len(ist):
      print("EOF")
      return "eof"
    if ist[count]==" ":
        count=count+1
        if count==len(ist):
          count=count-1
          return "eof"
        print("keno")
        print(count)
    if ist[count].isalpha():
      lektikh=lektikh+ist[count]
      count=count+1
      while ist[count].isalpha() or ist[count] in string.digits:
        lektikh=lektikh+ist[count]
        count=count+1
      #count=count+1
      print(count)
      if lektikh in ["if","while","repeat","exit","switch","forcase","call","return","input","print","program","endprogram","declare","enddeclare","procedure","endprocedure","function","endfunction","then","endif","endrepeat","in","inout","endswitch","endforcase","endwhile","ortk","andtk","nottk","truetk","falsetk","whentk","casetk","elsetk"] or ":=" in lektikh:
          print(count)
          return lektikh+"tk"
      print(count)
      print(lektikh)
      print(ist[count])
      return "idtk"
    elif ist[count] in string.digits:
      while ist[count] in string.digits:
        lektikh=lektikh+ist[count]
        count=count+1
      #count=count+1
      print(count)
      return lektikh+"constanttk"
    elif ist[count] in "+-*/=":
      lektikh=lektikh+ist[count]
      count=count+1
      print(count)
      return lektikh+"tk"
    elif ist[count] in"<":
      if ist[count+1] in "=>":
        lektikh=lektikh+ist[count]
        count=count+1
        lektikh=lektikh+ist[count]
        count=count+1
      else:
        lektikh=lektikh+ist[count]
        count=count+1
      print(count)
      return lektikh+"tk"
    elif ist[count] in">":
      if ist[count+1] in "=":
        lektikh=lektikh+ist[count]
        count=count+1
        lektikh=lektikh+ist[count]
        count=count+1	
      else:
        lektikh=lektikh+ist[count]
        count=count+1
        print(count)
        return lektikh+"tk"
    elif ist[count] in ":":
      if ist[count+1] in "=":
        lektikh=lektikh+ist[count]
        count=count+1
        lektikh=lektikh+ist[count]
        count=count+1
        print(count)
        return lektikh+"tk"
      else:
        count=count+1
        print("ERROR : WITHOUT = in "+count+"thesh")#ERROR
      return "error :="
		
    elif ist[count] in "{":
      lektikh=lektikh+ist[count]
      count=count+1
      while  ist[count]!="}":
        if count==len(ist):
          print("ERROR COMMENTS DONT CLOSE in "+count+"thesh")#ERROR
          return "error"
        lektikh=lektikh+ist[count]
        count=count+1
        lektikh=lektikh+ist[count]
        count=count+1
    elif ist[count] in ",;)(":
      lektikh=lektikh+ist[count]
      count=count+1
      print(count)
      return lektikh+"tk"
    else:
      print("------------------")
      print( ist)
      print(count)
      print("ERROR!")
      return "error"
##########end of lektikos
#main
    
#global count
#global ist

stringg=input('please input the name of program:')
print(stringg)
f=open(stringg+"","r")
for l in f:
  ist=ist+''+l
print(ist)
ist1=ist.split()
print(ist1)
ist=""
for i in ist1:
  ist=ist+" "+i
ist=ist+" "
print("------------------")
print(ist)
print("++++")
print(len(ist))

token=lektikos()
print("----------------------++++++++++++++++++++++++++++")



###########start def suntaktikou

def program():
  global token
  print("enter program with token="+token)
  if token=="programtk":
    token=lektikos()
    if token=="idtk":
      token=lektikos()
      block()
      if token=="endprogramtk":
        token=lektikos()
      else:
        print("error:the keyword ‘endprogram’ was expected")
    else:
      print("error:the name was expected")
  else:
    print("error:the keyword ‘program’ was expected")
  print("exit program with token="+token)
			
def block():
  global token
  print("enter block with token="+token)
  declarations()
  subprograms()
  statements()
  print("exit block with token="+token)


def declarations():
  global token
  print("enter declarations with token="+token)
  if token=="declaretk":
    token=lektikos()
    varlist()
    if token=="enddeclaretk":
      token=lektikos()		
    else:
      print("error:the keyword ‘enddeclare’ was expected")
  print("exit declarations with token="+token)
  
def varlist():
  global token
  print("enter varlist with token="+token)
  if token=="idtk":
    token=lektikos()
    while token==",tk":
      token=lektikos()
      if token=="idtk":
        token=lektikos()
  print("exit varlist with token="+token)				
				
def subprograms():
  global token
  print("enter subprograms with token="+token)
  while token=="proceduretk" or token=="functiontk":
    procorfunc()
  print("exit subprograms with token="+token)
  
def procorfunc():
  global token
  print("enter procorfunc with token="+token)
  if token=="proceduretk":
    token=lektikos()
    if token=="idtk":
      token=lektikos()
      procorfuncbody()
      if token=="endproceduretk":
        token=lektikos()
      else:
        print("error:the keyword ‘endprocedure’ was expected")
    else:
      print("error:the  name was expected")
  elif token=="functiontk":
    token=lektikos()
    if token=="idtk":
      token=lektikos()
      procorfuncbody()
      if token=="endfunctiontk":
        token=lektikos()
      else:
        print("error:the keyword ‘endfunction’ was expected")
    else:
      print("error:the  name was expected")
  else:
      print("error:the keyword ‘procedure’ or 'function' was expected")
  print("exit program with token="+token)
  
def procorfuncbody():
  global token
  print("enter procorfuncbody with token="+token)
  formalpars()
  block()
  print("exit procorfuncbody with token="+token)

def formalpars():
  global token
  print("enter formalpars with token="+token)
  if token=="(tk":
      token=lektikos()
      formalparlist()
      if token==")tk":
        token=lektikos()
      else:
        print("error:the  ‘)’ was expected")
  else:
    print("error:the  ‘)’ was expected")
  print("exit  formalpars with token="+token)
  
def formalparlist():
  global token
  print("enter formalparlist with token="+token)
  if token=="intk" or token=="inouttk":
    formalparitem()
    while token==",tk":
      token=lektikos()
      formalparitem()
  print("exit formalparlist with token="+token)


def formalparitem():
  global token
  print("enter formaloparitem with token="+token)
  if token=="intk":
    token=lektikos()
    if token=="idtk":
      token=lektikos()
    else:
      print("error:the name was expected")
  elif token=="inouttk":
    token=lektikos()
    if token=="idtk":
      token=lektikos()
    else:
      print("error:the name was expected")

  else:
    
    print("error:the keyword ‘in’ or 'inout' was expected")	
  print("exit formaloparitem with token="+token)
   
def statements():
  global token
  print("enter statements with token="+token)
  statement()
  while token==";tk":
    token=lektikos()
    statement()
  print("exit statements with token="+token)
  
def statement():
  global token
  print("enter statement with token="+token)
  if token== "idtk":
    assignment_stat()
  elif token=="iftk":
    if_stat()
  elif token=="whiletk":
    while_stat()
  elif token=="repeattk":
    repeat_stat()
  elif token=="exittk":
    exit_stat()
  elif token=="switchtk":
    switch_stat()
  elif token=="forcasetk":
    forcase_stat()
  elif token=="calltk":
    call_stat()
  elif token=="returntk":
    return_stat()
  elif token=="inputtk":
    input_stat()
  elif token=="printtk":
    print_stat()
  print("exit statement with token="+token)
    


def assignment_stat():
  global token
  print("enter assignment_stat with token="+token)
  token=lektikos()
  if token==":=tk":
    token=lektikos()
    expression()
  else:
    print("error:the  ‘:=’ ' was expected!")
  print("exit assignment_stat with token="+token)
  
def if_stat():
  global token
  print("enter if_stat with token="+token)
  token=lektikos()
  condition()
  if token=="thentk":
    token=lektikos()
    statements()
    if token=="elsetk":
      token=lektikos()
      elsepart()
    if token=="endiftk":
      token=lektikos()
    else:
      print("error:the keyword ‘endif’  was expected")
  else:
    print("error:the keyword ‘then’  was expected")
  print("exit if_stat with token="+token)
  
def elsepart():
  global token
  print("enter elsepart with token="+token)
  #token=lektikos()
  statements()
  print("exit elsepart with token="+token)



def repeat_stat():
  global token
  print("enter repeat_stat with token="+token)
  token=lektikos()
  statements()
  if token=="endrepeattk":
    token=lektikos()
  else:
    print("error:the keyword ‘endrepeat’  was expected")
  print("exit repeat_stat with token="+token)
  
def exit_stat():
  global token
  print("enter exit_stat with token="+token)
  token=lektikos()
  print("exit exit_stat with token="+token)

def while_stat():
  global token
  print("enter while_stat with token="+token)
  token=lektikos()
  condition()
  statements()
  if token=="endwhiletk":
    token=lektikos()
  else:
    print("error:the keyword ‘endwhile’  was expected") 
  print("exit while_stat with token="+token)

def switch_stat():
  global token
  print("enter switch_stat with token="+token)
  token=lektikos()
  expression()
  if token=="casetk":
    token=lektikos()
    expression()
    statements()
    while token=="casetk":
      token=lektikos()
      expression()
      statements()
    if token=="endswitchtk":
      token=lektikos()
    else:
        print("error:the keyword ‘endswitch’  was expected")
  else:
    print("error:the keyword ‘case’  was expected")
  print("exit switch_stat with token="+token)
  
def forcase_stat():
  global token
  print("enter forcase_stat with token="+token)
  token=lektikos()
  if token=="whentk":
    token=lektikos()
    condition()
    statements()
    while token=="whentk":
      token=lektikos()
      condition()
      statements()
    if token=="endforcasetk":
      token=lektikos()
    else:
        print("error:the keyword ‘endforcase’  was expected")
  else:
    print("error:the keyword ‘when’  was expected")
  print("exit forcase_stat with token="+token)
  
def call_stat():
  global token
  print("enter call_stat with token="+token)
  token=lektikos()
  if token=="idtk":
    token=lektikos()
    actualpars()
  else:
    print("error:the name  was expected")
  print("exit call_stat with token="+token)
def return_stat():
  global token
  print("enter return_stat with token="+token)
  token=lektikos()
  expression()
  print("exit return_stat with token="+token)
def print_stat():
  global token
  print("enter print_stat with token="+token)
  token=lektikos()
  expression()
  print("exit print_stat with token="+token)
    
def input_stat():
  global token
  print("enter input_stat with token="+token)
  token=lektikos()
  if token=="idtk":
    token=lektikos()
  else:
    print("error:the  name(id)  was expected")
  print("exit input_stat with token="+token)

def actualpars():
  global token
  print("enter actualpars with token="+token)
  if token=="(tk":
    token=lektikos()
    actualparlist()
    if token==")tk":
      token=lektikos()

    else:
      print("error:the keyword ‘)’  was expected")
  else:
    print("error:the keyword ‘(’  was expected")
  print("exit actualpars with token="+token) 
          
def actualparlist():
  global token
  print("enter actualparlist with token="+token)
  if token=="intk" or token=="inouttk":
    actualparitem()
    while token==",tk":
      token=lektikos()
      actualparitem()
 
  print("exit actualparlist with token="+token)      

def actualparitem():
  global token
  print("enter actualparitem with token="+token)
  if token=="intk":
    token=lektikos()
    expression()
  elif token=="inouttk":
    token=lektikos()
    if token=="idtk":
      token=lektikos()
    else:
      print("error:the name id   was expected")
  print("exit actualparitem with token="+token)
   
def return_stat():
  global token
  print("enter return_stat with token="+token)
  token=lektikos()
  expression()
  print("exit return_stat with token="+token)

def condition():
  global token
  print("enter condition with token="+token)
  boolterm()
  while token=="ortk":
    token=lektikos()
    boolterm()
  print("exit condition with token="+token)

def boolterm():
  global token
  print("enter boolterm with token="+token)
  boolfactor()
  while token=="andtk":
    token=lektikos()
    boolfactor()
  print("exit boolterm with token="+token)

def boolfactor():
  global token
  print("enter boolfactor with token="+token)
  if token=="nottk":
    token=lektikos()
    if token=="[tk":
      token=lektikos()
      condition()
      if token=="]tk":
        token=lektikos()
      else:
        print("error:the keyword ‘]’  was expected")
          
    else:
      print("error:the keyword ‘[’  was expected")
  elif token=="[tk":
    token=lektikos()
    condition()
    if token=="]tk":
      token=lektikos()
    else:
      print("error:the keyword ‘]’  was expected")
  elif token=="truetk":
    token=lektikos()
  elif token=="falsetk":
    token=lektikos()
  else:
    expression()
    relational_oper()
    expression()  
  print("exit boolfactor with token="+token)
  
def expression():
  global token
  print("enter expression with token="+token)
  optional_sign()
  term()
  while token=="+tk" or token=="-tk":
    add_oper()
    term()
  print("exit expression with token="+token)
  
def term():
  global token
  print("enter term with token="+token)
  factor()
  while token=="*tk" or token=="/tk":
    mul_oper()
    factor()
  print("exit term with token="+token)


def factor():
  global token
  print("enter factor with token="+token)
  if "constanttk" in token:
    token=lektikos()
  elif token=="(tk":
    token=lektikos()
    expression()
    if token==")tk":
      token=lektikos()
    else:
      print("error:the keyword ‘)’  was expected")
  elif token=="idtk":
    token=lektikos()
    idtail()
  else:
    print("error:the keyword ‘(’  was expected")
  print("exit factor with token="+token)
  
def idtail():
  global token
  print("enter idtail with token="+token)
  if token=="(tk":
    actualpars()
  print("exit idtail with token="+token)

def relational_oper():
  global token
  print("enter relational_oper with token="+token)
  if token=="=tk" or token=="<=tk" or  token==">=tk" or token==">tk" or token=="<tk" or token=="<>tk" :
    token=lektikos()
  else:
    print("error:one of the keywords ‘=,<=,>=, <,>,<>’  was expected")
  print("exit relational_oper with token="+token)
  
def add_oper():
  global token
  print("enter add_oper with token="+token)
  if token=="+tk" or token=="-tk":
    token=lektikos()
  else:
    print("error:one of the keywords ‘+,-’  was expected")
  print("exit add_oper with token="+token)
  
def mul_oper():
  global token
  print("enter mul_oper with token="+token)
  if token=="*tk" or token=="/tk":
    token=lektikos()
  else:
    print("error:one of the keywords ‘*,/’  was expected")
  print("exit mul_oper with token="+token)
  
def optional_sign():
  global token
  print("enter optional_sign with token="+token)
  if token=="+tk" or token=="-tk":
    add_oper()
  print("exit optional_sign with token="+token)
    
################ EXECUTE
print("----------------------------------")
print(ist[239])
print(ist[238],ist[239],ist[240],ist[241],ist[242],ist[243])
program()

      
    
	


	


















 	
